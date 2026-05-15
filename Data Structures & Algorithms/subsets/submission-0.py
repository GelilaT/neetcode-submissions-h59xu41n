class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = [[]]
        def backtrack(i, path):
            
            if i == len(nums):
                return

            path.append(nums[i])
            for j in range(i + 1, len(nums)):
                backtrack(j, path)
                path.pop()

            ans.append(path.copy())

        for i in range(len(nums)):
            backtrack(i, [])

        return ans


        