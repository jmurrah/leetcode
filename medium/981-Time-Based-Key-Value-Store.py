"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

    TimeMap() Initializes the object of the data structure.
    void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
    String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it 
    returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

"""


class TimeMap:

    def __init__(self):
        self.keys = defaultdict(dict)
        self.timestamps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].append(timestamp)
        self.keys[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.timestamps[key]
        l, r = 0, len(timestamps) - 1

        while l <= r:
            m = (l + r) // 2
            if timestamps[m] <= timestamp:
                l = m + 1
            else:
                r = m - 1
        
        return "" if r == -1 else self.keys[key][timestamps[l-1]]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
