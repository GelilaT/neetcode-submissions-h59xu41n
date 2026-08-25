class TimeMap:

    def __init__(self):
        self.keys = set()
        self.pairs = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys.add(key)
        self.pairs[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.keys:
            return ""

        n = len(self.pairs[key])
        low, high = 0, n - 1
        while low <= high:
            mid = low + (high - low) // 2
            val = self.pairs[key][mid][1]
            if val > timestamp:
                high = mid - 1

            elif val < timestamp:
                low = mid + 1

            else:
                return self.pairs[key][mid][0]

        idx = low - 1
        return self.pairs[key][idx][0] if idx >= 0 else ""
