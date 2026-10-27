import bisect

class TimeMap:

    def __init__(self):
        self.key_val = dict()
        self.key_ts = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_val:
            self.key_val[key] = [value]
            self.key_ts[key] = [timestamp]
        else:
            self.key_val[key].append(value)
            self.key_ts[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_val:
            return ""
        idx = bisect.bisect_right(self.key_ts[key], timestamp)
        if idx == len(self.key_ts[key]):
            return self.key_val[key][idx-1]
        elif idx == 0 and self.key_ts[key][idx] != timestamp:
            return ""
        elif self.key_ts[key][idx] == timestamp:
            return self.key_val[key][idx]
        else:
            return self.key_val[key][idx-1]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
