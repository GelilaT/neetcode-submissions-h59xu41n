class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        XOR = 0
        for i in range(1, len(nums) + 1):
            XOR ^= i

        for num in nums:
            XOR ^= num

        return XOR
      
      