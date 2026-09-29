class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        ans = set()
        def backtrack(path, visited):

            if len(path) == len(nums):
                ans.add(tuple(path.copy()))
                return

            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    path.append(nums[i])
                    backtrack(path, visited)
                    visited.remove(i)
                    path.pop()

        backtrack([], set())
        return [list(val) for val in ans]
        