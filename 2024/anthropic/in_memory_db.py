import math
class Record:
    key: str
    value: str
    timestamp: int 
    expire: int = math.inf

class InMemoDb:
    def __init__(self):
        self.memo = {}
        from collections import defaultdict
        self.record_versions = defaultdict(list)

    def set(self, key, value, timestamp):
        self.memo[key] = Record(key, value, timestamp)
        self.record_versions[key].append(self.memo[key])

    def get(self, key, timestamp):
        if key not in self.memo:
            return False
        if timestamp < self.memo[key].expire:
            return self.memo[key].value
        self.delete(key)
        return False
    
    def delete(self, key):
        if key not in self.memo:
            return False
        self.record_versions[key].append(self.memo[key])
        del self.memo[key]
        return True
    
    def set_with_ttl(self, key, val, timestamp, ttl):
        self.memo[key] = Record(key, value, expire=timestamp + ttl, timestamp=timestamp)
        self.record_versions[key].append(self.memo[key])
    
    def scan(self):
        return self._scan(self.memo.values())
    

    def _scan(self, values):
        sorted_records = sorted(values, key = lambda v: v.key)
        return [f"{r.key}:{r.value}" for r in sorted_records]
    
    def scan_wth_prefix(self, prefix):
        records = filter(lambda v: v.startswith(prefix), self.memo.values) 
        return self._scan(records)

    def restore(self, timestamp):
        




