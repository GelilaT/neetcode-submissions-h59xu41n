class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        ans = set()
        def backtrack(i, path):
            
            if sum(path) == target:
                ans.add(tuple(path.copy()))
                return

            if i >= len(nums) or sum(path) > target:
                return

            backtrack(i + 1, path + [nums[i]])
            backtrack(i + 1, path)
            backtrack(i, path + [nums[i]])


        backtrack(0, [])
        return [list(t) for t in ans]
        