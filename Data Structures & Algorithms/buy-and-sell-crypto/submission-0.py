class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_prize = math.inf
        max_profit = 0
        for num in prices:

            min_prize = min(num, min_prize)
            max_profit = max(max_profit, num - min_prize)

        return max_profit

        