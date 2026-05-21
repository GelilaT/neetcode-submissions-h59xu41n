class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}
        def dfs(total):
            
            nonlocal ans
            if total == amount:
                return 0

            if total in memo:
                return memo[total]

            res = math.inf
            for coin in coins:
                if total + coin <= amount:
                    res = min(res, 1 + dfs(total + coin))

            memo[total] = res
            return res

        ans = dfs(0)
        return ans if ans != math.inf else -1
            
        