class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ans = set()
        nums.sort()
        def backtrack(idx, path):

            if idx >= len(nums):
                ans.add(tuple(path.copy()))
                return

            backtrack(idx + 1, path + [nums[idx]])
            backtrack(idx + 1, path)

        backtrack(0, [])
        return [list(val) for val in ans]

        