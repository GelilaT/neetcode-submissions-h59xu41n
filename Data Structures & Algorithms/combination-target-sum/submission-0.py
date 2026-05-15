class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        ans = set()
        def backtrack(i, path, target):
            
            if target == 0:
                ans.add(tuple(path.copy()))
                return

            if target < 0:
                return

            if i >= len(nums):
                return

            backtrack(i + 1, path + [nums[i]], target - nums[i])
            backtrack(i + 1, path, target)
            backtrack(i, path + [nums[i]], target - nums[i])


        backtrack(0, [], target)
        return [list(t) for t in ans]
        