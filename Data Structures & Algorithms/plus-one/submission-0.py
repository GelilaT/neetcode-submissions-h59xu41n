class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        def helper(nums):
 
            n, degree = len(nums), len(nums) - 1
            num = 0
            for i in range(n):
                multiplier = 10 ** degree
                num += (nums[i] * multiplier)
                degree -= 1

            return num

        n = helper(digits) + 1
        ans = []
        while n >= 10:
            ans.append(n % 10)
            n //= 10

        ans.append(n)
        return ans[::-1]





        