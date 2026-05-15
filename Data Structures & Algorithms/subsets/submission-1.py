class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []
        def backtrack(i, path):
            
            if i >= len(nums):
                ans.append(path)
                return

            backtrack(i + 1, path + [nums[i]])
            backtrack(i + 1, path)

        backtrack(0, [])
        return ans


        