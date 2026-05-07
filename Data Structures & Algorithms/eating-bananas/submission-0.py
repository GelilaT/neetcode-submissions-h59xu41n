class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def getTotalHours(k):

            total = 0
            for i in piles:
                total += (math.ceil(i / k))

            return total

        low, high = 1, max(piles)
        while low <= high:
            mid = low + (high - low) // 2
            if getTotalHours(mid) <= h:
                high = mid - 1

            else:
                low = mid + 1

        return low
        