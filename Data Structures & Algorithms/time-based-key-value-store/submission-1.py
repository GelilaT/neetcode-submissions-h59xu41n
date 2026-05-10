class TimeMap:

    def __init__(self):
        self.my_dict = defaultdict(str)
        self.time = defaultdict(list)
        self.keys = set()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.my_dict[(key, timestamp)] = value
        self.time[key].append(timestamp)
        self.keys.add(key)

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.keys:
            return ""

        times = self.time[key]
        low, high = 0, len(times)

        while low < high:
            mid = low + (high - low) // 2

            if times[mid] <= timestamp:
                low = mid + 1
            else:
                high = mid

        idx = low - 1

        return self.my_dict[(key, times[idx])] if idx >= 0 else ""

