class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def checker(n):

            time = 0
            for pile in piles:
                time += math.ceil(pile / n)

            return time <= h

        low, high = 1, max(piles)
        while low <= high:

            mid = low + (high - low) // 2
            if checker(mid):
                high = mid - 1

            else:
                low = mid + 1

        return low

