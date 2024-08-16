from collections import deque
from time import time
import bisect


class HitCounter:
    def __init__(self, interval=300):
        """
        Initialize the hit counter.

        :param interval: The time frame window (in seconds) during which hits are counted.
        """
        self.hits = []
        self.interval = interval

    def hit(self):
        """
        Record a hit at the current timestamp.
        """
        current_time = int(time())
        self.hits.append(current_time)

    def get_hits(self):
        """
        Return the number of hits in the last `interval` seconds.

        :return: The number of hits in the last `interval` seconds.
        """
        current_time = int(time())
        self._remove_old_hits(current_time)
        return len(self.hits)

    def _remove_old_hits(self, current_time):
        """
        Helper method to remove hits that are older than the `interval` timeframe.

        :param current_time: The current timestamp to compare against.
        """
        threshold_time = current_time - self.interval
        index = bisect.bisect_left(self.hits, threshold_time)

        # Remove all hits before the index
        self.hits = self.hits[index:]

# Example Usage:

counter = HitCounter()

# Simulating hits
counter.hit()
print("Hits after 1st hit:", counter.get_hits())  # Should print 1

# Wait some time and then record another hit
import time as t
t.sleep(1)
counter.hit()
print("Hits after 2nd hit:", counter.get_hits())  # Should print 2

# Simulate waiting for the interval to expire
t.sleep(300)
print("Hits after 300 seconds:", counter.get_hits())  # Should print 0 if interval is 300 seconds