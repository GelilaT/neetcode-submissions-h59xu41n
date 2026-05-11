class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        maxi = max(nums)
        bucket = [0] * maxi
        for num in nums:
            if bucket[num - 1] != 0:
                return num

            else:
                bucket[num - 1] += 1

                