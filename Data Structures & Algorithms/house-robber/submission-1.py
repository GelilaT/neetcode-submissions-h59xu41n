class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}
        n = len(nums)
        def dp(i):

            if i == 0:
                return nums[i]

            if i == 1:
                return max(nums[1], nums[0])
                
            if i in memo:
                return memo[i]

            memo[i] = max(dp(i - 1), nums[i] + dp(i - 2))
            return memo[i]

        return dp(n - 1)
        