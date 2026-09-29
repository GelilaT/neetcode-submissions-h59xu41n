class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        def backtrack(visited, path):

            if len(path) == len(nums):
                ans.append(path.copy())
                return

            for num in nums:
                if num not in visited:
                    path.append(num)
                    visited.add(num)
                    backtrack(visited, path)
                    path.pop()
                    visited.remove(num)

        backtrack(set(), [])
        return ans

            
        