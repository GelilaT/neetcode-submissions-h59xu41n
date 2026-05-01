class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # -4, -1, -1, 0, 1, 2
        nums.sort()
        n = len(nums)
        ans = set([])
        for i in range(n):
            l, r = i + 1, n - 1
            while l < r:
                if -nums[i] < nums[l] + nums[r]:
                    r -= 1

                elif -nums[i] > nums[l] + nums[r]:
                    l += 1

                else:
                    ans.add(tuple(sorted((nums[i], nums[l], nums[r]))))
                    l += 1
                    r -= 1
        
        return [list(t) for t in ans]