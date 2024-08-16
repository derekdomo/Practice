from datetime import datetime, timedelta
import bisect
from collections import defaultdict
from threading import Lock

class HitCounter:
    def __init__(self, interval=300):
        """
        Initialize the hit counter.

        :param interval: The time frame window (in seconds) during which hits are counted.
        """
        self.hits_by_platform = defaultdict(lambda: defaultdict(int))  # platform -> date -> hit count
        self.prefix_sums = defaultdict(list)  # platform -> list of (date, cumulative hit count)
        self.interval = interval
        self.timestamps = set()
        self.lock = Lock()  # Thread lock for thread-safety

    def hit(self, timestamp, count, platform):
        """
        Record a hit at the given timestamp with a specified count for a specific platform.

        :param timestamp: The timestamp when the hit occurred.
        :param count: The number of hits to record for the given timestamp.
        :param platform: The platform for which the hit is recorded.
        """
        date = datetime.strptime(timestamp, "%Y-%m-%d")
        with self.lock:
            self.hits_by_platform[platform][date] += count
            self.timestamps.add(date)

    def build_prefix_sums(self):
        """
        Build the prefix sums for each platform. This should be called after all hits have been recorded.
        """
            for platform in self.hits_by_platform:
                sorted_dates = sorted(self.hits_by_platform[platform])
                cumulative_hit_count = 0
                self.prefix_sums[platform] = []  # Reset prefix sums
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
        with self.lock:
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

import threading

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

# Function to record hits in parallel
def record_hits():
    for date, platforms in raw_log.items():
        for platform, stats in platforms.items():
            counter.hit(date, stats['pageViewCount'], platform)

# Create and start multiple threads to simulate concurrent recording of hits
threads = [threading.Thread(target=record_hits) for _ in range(5)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

# Build prefix sums after recording all hits
counter.build_prefix_sums()

# Function to query hits in parallel
def query_hits():
    print("Total hits within the interval:", counter.get_hits("2022-06-14"))  # Total hits across all platforms
    print("iOS hits within the interval:", counter.get_hits("2022-06-14", "ios"))  # Hits for iOS platform
    print("Reddit web hits within the interval:", counter.get_hits("2022-06-14", "reddit web"))  # Hits for Reddit web platform

# Create and start multiple threads to simulate concurrent querying of hits
threads = [threading.Thread(target=query_hits) for _ in range(5)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

# Simulate waiting for the interval to expire
old_date = (datetime.strptime("2022-06-14", "%Y-%m-%d") + timedelta(days=301)).strftime("%Y-%m-%d")
print("Total hits within the interval after expiration:", counter.get_hits(old_date))  # Should print 0
print("iOS hits within the interval after expiration:", counter.get_hits(old_date, "ios"))  # Should print 0
print("Reddit web hits within the interval after expiration:", counter.get_hits(old_date, "reddit web"))  # Should print 0