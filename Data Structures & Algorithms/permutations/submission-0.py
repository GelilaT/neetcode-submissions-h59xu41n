class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        def dfs(path, visited):

            if len(path) == len(nums):
                ans.append(path.copy())
                return

            for idx in range(len(nums)):
                if nums[idx] not in visited:
                    path.append(nums[idx])
                    visited.add(nums[idx])
                    dfs(path, visited)
                    path.pop()
                    visited.remove(nums[idx])

        dfs([], set())
        return ans



        