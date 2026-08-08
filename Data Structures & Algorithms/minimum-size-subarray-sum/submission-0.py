class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left, min_len = 0, math.inf
        summ = 0
        for right in range(len(nums)):
            summ += nums[right]
            while summ >= target:
                summ -= nums[left]
                min_len = min(min_len, right - left + 1)
                left += 1

        return min_len if min_len != math.inf else 0

        