class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_val = prices[0]
        max_profit = 0
        for right in range(1, len(prices)):
            
            profit = prices[right] - min_val
            max_profit = max(profit, max_profit)
            min_val = min(min_val, prices[right])

        return max_profit




        