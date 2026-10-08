class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        memo = {}
        cost.append(0)
        def dp(i):

            if i == 0 or i == 1:
                return cost[i]

            if i in memo:
                return memo[i]

            memo[i] = min(dp(i - 1), dp(i - 2)) + cost[i]
            return memo[i]

        return dp(len(cost) - 1)

        