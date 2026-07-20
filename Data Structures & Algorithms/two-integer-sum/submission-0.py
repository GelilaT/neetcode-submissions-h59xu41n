class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        my_dict = {}
        for i, num in enumerate(nums):
            if num in my_dict:
                return [my_dict[num], i]

            diff = target - num
            my_dict[diff] = i
        