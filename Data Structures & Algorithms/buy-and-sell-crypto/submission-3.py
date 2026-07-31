class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0
        max_profit = 0
        for right in range(len(prices)):
            
            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)

            if prices[right] < prices[left]:
                left = right

        return max_profit




        