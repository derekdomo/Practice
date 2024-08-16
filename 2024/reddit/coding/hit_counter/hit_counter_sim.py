from datetime import datetime, timedelta
import bisect
from collections import defaultdict

class HitCounter:
    def __init__(self, interval=300):
        """
        Initialize the hit counter.

        :param interval: The time frame window (in seconds) during which hits are counted.
        """
        self.hits_by_platform = defaultdict(lambda: defaultdict(int))  # platform -> date -> hit count
        self.interval = interval
        self.timestamps = set()
        self.prefix_sums = defaultdict(list)  # platform -> list of (date, cumulative hit count)

    def hit(self, timestamp, count, platform):
        """
        Record a hit at the given timestamp with a specified count for a specific platform.

        :param timestamp: The timestamp when the hit occurred.
        :param count: The number of hits to record for the given timestamp.
        :param platform: The platform for which the hit is recorded.
        """
        date = datetime.strptime(timestamp, "%Y-%m-%d")
        self.hits_by_platform[platform][date] += count
        self.timestamps.add(date)

    def build_prefix_sums(self):
        """
        Build the prefix sums for each platform. This should be called after all hits have been recorded.
        """
        for platform in self.hits_by_platform:
            sorted_dates = sorted(self.hits_by_platform[platform])
            cumulative_hit_count = 0
            for date in sorted_dates:
                cumulative_hit_count += self.hits_by_platform[platform][date]
                self.prefix_sums[platform].append((date, cumulative_hit_count))

    def get_hits(self, current_time, platform=None):
        """
        Return the number of hits in the last `interval` seconds relative to the given current time.

        :param current_time: The current timestamp for comparison.
        :param platform: The platform for which to get the hits counts. If None, returns total count across all platforms.
        :return: The number of hits in the last `interval` seconds.
        """
        current_timestamp = datetime.strptime(current_time, "%Y-%m-%d")
        threshold_time = current_timestamp - timedelta(seconds=self.interval)

        if platform:
            return self._get_hits_for_platform(threshold_time, current_timestamp, platform)

        total_hits = 0
        for platform in self.hits_by_platform:
            total_hits += self._get_hits_for_platform(threshold_time, current_timestamp, platform)

        return total_hits

    def _get_hits_for_platform(self, threshold_time, current_timestamp, platform):
        """
        Helper method to get the number of hits within the interval for a specific platform.

        :param threshold_time: The start of the interval.
        :param current_timestamp: The current timestamp.
        :param platform: The platform for which to get the hits.
        :return: The number of hits in the interval for the specified platform.
        """
        prefix_sum = self.prefix_sums[platform]
        if not prefix_sum:
            return 0

        start_index = bisect.bisect_left(prefix_sum, (threshold_time,))  # Find first index >= threshold_time
        end_index = bisect.bisect_right(prefix_sum, (current_timestamp,)) - 1  # Find last index <= current_timestamp

        if start_index == len(prefix_sum) or prefix_sum[start_index][0] > current_timestamp:
            return 0

        start_hits = prefix_sum[start_index][1] if start_index > 0 else 0
        end_hits = prefix_sum[end_index][1] if end_index >= 0 else 0

        return end_hits - start_hits

# Example Usage:

# Initializing the raw_log
raw_log = {
    "2022-06-13": {
        "ios": {
            "pageViewCount": 20000,
            "unique": 12999
        },
        "reddit web": {
            "pageViewCount": 20000,
            "unique": 12999
        }
    },
    "2022-06-11": {
        "ios": {
            "pageViewCount": 20000,
            "unique": 12999
        },
        "reddit web": {
            "pageViewCount": 20000,
            "unique": 12999
        }
    },
    "2022-06-10": {
        "ios": {
            "pageViewCount": 20000,
            "unique": 12999
        },
        "reddit web": {
            "pageViewCount": 20000,
            "unique": 12999
        }
    },
    "2022-06-06": {
        "ios": {
            "pageViewCount": 20000,
            "unique": 12999
        },
        "reddit web": {
            "pageViewCount": 20000,
            "unique": 12999
        }
    },
    "2022-01-12": { 
        "ios": {
            "pageViewCount": 20000,
            "unique": 12999
        },
        "reddit web": {
            "pageViewCount": 20000,
            "unique": 12999
        }
    }
}

counter = HitCounter(interval=300*24*60*60)  # Setting interval to 300 days for this example

# Simulating hits from raw_log
for date, platforms in raw_log.items():
    for platform, stats in platforms.items():
        counter.hit(date, stats['pageViewCount'], platform)

# Build prefix sums after recording all hits
counter.build_prefix_sums()

# Get hits within the last interval (300 days from "2022-06-14")
print("Total hits within the interval:", counter.get_hits("2022-06-14"))  # Total hits across all platforms
print("iOS hits within the interval:", counter.get_hits("2022-06-14", "ios"))  # Hits for iOS platform
print("Reddit web hits within the interval:", counter.get_hits("2022-06-14", "reddit web"))  # Hits for Reddit web platform

# Simulate waiting for the interval to expire
old_date = (datetime.strptime("2022-06-14", "%Y-%m-%d") + timedelta(days=301)).strftime("%Y-%m-%d")
print("Total hits within the interval after expiration:", counter.get_hits(old_date))  # Should print 0
print("iOS hits within the interval after expiration:", counter.get_hits(old_date, "ios"))  # Should print 0
print("Reddit web hits within the interval after expiration:", counter.get_hits(old_date, "reddit web"))  # Should print 0




class HitCounter:
    def __init__(self, last_k_days):
        # can use prefix sum if the log is processed in chronological order
        self.last_k_days = last_k_days
        self.logs = []
        self.prefix_sum = []

    def process_log(self, date, log):
        fs_ind = self._find_first_smaller_date(date)
        self.logs = self.logs[:fs_ind+1] + [(date, log)] + self.logs[fs_ind+1:]

    def process_log_chrono(self, date, log):
        self.logs.append((date, log))
        last_sum = {}
        if len(self.prefix_sum) > 0:
            last_sum = self.prefix_sum[-1][1].copy()

        for platform, view in log.items():
            if platform not in last_sum:
                last_sum[platform] = {
                    'pageViewCount': 0,
                    'unique': 0
                }
            last_sum[platform]['pageViewCount'] += view['pageViewCount']
            last_sum[platform]['unique'] += view['unique']
        self.prefix_sum.append((date, last_sum))

        
    def _find_first_smaller_date(self, date: str) -> int:
        left = 0 
        right = len(self.logs) - 1
        result = -1
        while left <= right:
            mid = left + (right - left)//2
            if self.logs[mid][0] < date:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result 

    def _find_first_larger_date(self, date: str) -> int:
        left = 0
        right = len(self.logs) - 1
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            if self.logs[mid][0] > date:
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result
    
    def get_hit_counts(self, date):
        from datetime import datetime, timedelta
        now = datetime.strptime(date, "%Y-%m-%d")
        most_recent_day = datetime.strftime(now - timedelta(self.last_k_days-1), '%Y-%m-%d')
        agg_result = {}
        fs_ind = self._find_first_smaller_date(most_recent_day)
        for i in range(fs_ind+1, len(self.logs)):
            for platform, view in self.logs[i][1].items():
                if platform not in agg_result:
                    agg_result[platform] = {
                        'pageViewCount': 0,
                        'unique': 0
                    }
                agg_result[platform]['pageViewCount'] += view['pageViewCount']
                agg_result[platform]['unique'] += view['unique']

        return agg_result
    
    def get_hit_counts_chrono(self, date):
        from datetime import datetime, timedelta
        now = datetime.strptime(date, "%Y-%m-%d")
        most_recent_day = datetime.strftime(now - timedelta(self.last_k_days-1), '%Y-%m-%d')
        fs_ind = self._find_first_smaller_date(most_recent_day)
        last_sum = self.prefix_sum[-1][1].copy()
        for platform, view in self.logs[fs_ind][1].items():
            last_sum[platform]['pageViewCount'] -= view['pageViewCount']
            last_sum[platform]['unique'] -= view['unique']
        return last_sum





raw_log = {
    "2022-06-13": {
        "ios": {
            "pageViewCount": 20000,
            "unique": 12999
        },
        "reddit web": {
            "pageViewCount": 20000,
            "unique": 12999
        }
    },
    "2022-06-11": {
        "ios": {
            "pageViewCount": 20000,
            "unique": 12999
        },
        "reddit web": {
            "pageViewCount": 20000,
            "unique": 12999
        }
    },
    "2022-06-10": {
        "ios": {
            "pageViewCount": 20000,
            "unique": 12999
        },
        "reddit web": {
            "pageViewCount": 20000,
            "unique": 12999
        }
    },
    "2022-06-06": {
        "ios": {
            "pageViewCount": 20000,
            "unique": 12999
        },
        "reddit web": {
            "pageViewCount": 20000,
            "unique": 12999
        }
    },
    "2022-01-12": { 
        "ios": {
            "pageViewCount": 20000,
            "unique": 12999
        },
        "reddit web": {
            "pageViewCount": 20000,
            "unique": 12999
        }
    }
}

hit_counter = HitCounter(7)
for d, log in raw_log.items():
    hit_counter.process_log_chrono(d, log)
print(hit_counter.get_hit_counts_chrono('2022-06-13'))


