class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def capacity(mid):

            day = 1
            cur = mid
            for i in range(len(weights)):
                if cur - weights[i] < 0:
                    day += 1
                    cur = mid
                
                cur -= weights[i]
            
            return day 

        low, high = max(weights), sum(weights)
        while low <= high:
            mid = low + (high - low) // 2
            if capacity(mid) <= days:
                high = mid - 1
            else:
                low = mid + 1

        return low

        