class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []
        def backtrack(idx, path):

            if idx >= len(nums):
                ans.append(path)
                return
                
            backtrack(idx + 1, path + [nums[idx]])
            backtrack(idx + 1, path)

        backtrack(0, [])
        return ans

            


        