class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        memo = {}
        def dp(i, state):

            if i == n:
                return 0

            if (i, state) in memo:
                return memo[(i, state)]

            jump = dp(i + 1, state)
            if state:
                buy = dp(i + 1, not state) - prices[i]
                memo[(i, state)] = max(buy, jump)

            else:
                sell = dp(i + 1, not state) + prices[i]
                memo[(i, state)] = max(sell, jump)

            return memo[(i, state)]

        return dp(0, True)

        
