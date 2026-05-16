class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ans = set()
        nums.sort()
        def dfs(i, path):

            if i == len(nums):
                ans.add(tuple(path.copy()))
                return

            dfs(i + 1, path + [nums[i]])
            dfs(i + 1, path)

        dfs(0, [])
        return [list(t) for t in ans]


        