import threading
import time
from bisect import bisect_right
from collections import deque

class ThreadSafeHitCounter:
    def __init__(self):
        self.hits = deque()  # A deque to keep track of hit timestamps
        self.lock = threading.Lock()  # Lock to protect access to the deque

    def hit(self):
        """Record a new hit at the current timestamp."""
        current_time = int(time.time())
        with self.lock:
            self.hits.append(current_time)

    def _purge_old_hits(self, current_time, last_n_seconds):
        """
        Internal method to remove hits older than last_n_seconds.
        """
        cutoff_time = current_time - last_n_seconds
        valid_hits_index = bisect_right(self.hits, cutoff_time)
        self.hits = deque(list(self.hits)[valid_hits_index:])

    def get_hits(self, last_n_seconds=300):
        """
        Get the number of hits in the last 'last_n_seconds' seconds.
        Default is the last 5 minutes (300 seconds).
        """
        current_time = int(time.time())

        with self.lock:
            self._purge_old_hits(current_time, last_n_seconds)
            hits_count = len(self.hits)

        return hits_count

# Example usage:
# counter = ThreadSafeHitCounter()
# counter.hit()
# time.sleep(1)
# print(counter.get_hits()) 



import threading

class ReaderWriterLock:
    def __init__(self):
        self.condition = threading.Condition()
        self.readers = 0

    def acquire_read(self):
        with self.condition:
            self.readers += 1

    def release_read(self):
        with self.condition:
            self.readers -= 1
            if self.readers == 0:
                self.condition.notify_all()

    def acquire_write(self):
        self.condition.acquire()
        while self.readers > 0:
            self.condition.wait()

    def release_write(self):
        self.condition.release()


class ThreadSafeHitCounter:
    def __init__(self):
        self.hits = deque()  # A deque to keep track of hit timestamps
        self.rw_lock = ReaderWriterLock()  # Reader-Writer lock for synchronization

    def hit(self):
        """Record a new hit at the current timestamp."""
        current_time = int(time.time())
        self.rw_lock.acquire_write()
        try:
            self.hits.append(current_time)
        finally:
            self.rw_lock.release_write()

    def _purge_old_hits(self, current_time, last_n_seconds):
        """
        Internal method to remove hits older than last_n_seconds.
        """
        cutoff_time = current_time - last_n_seconds
        valid_hits_index = bisect_right(self.hits, cutoff_time)
        self.hits = deque(list(self.hits)[valid_hits_index:])

    def get_hits(self, last_n_seconds=300):
        """
        Get the number of hits in the last 'last_n_seconds' seconds.
        Default is the last 5 minutes (300 seconds).
        """
        current_time = int(time.time())
        self.rw_lock.acquire_write()
        try:
            self._purge_old_hits(current_time, last_n_seconds)
        finally:
            self.rw_lock.release_write()

        self.rw_lock.acquire_read()
        try:
            hits_count = len(self.hits)
        finally:
            self.rw_lock.release_read()

        return hits_count
