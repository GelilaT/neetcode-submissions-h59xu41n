class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ans = set()
        for i in range(len(nums)):

            target = -nums[i]
            j, k = i + 1, len(nums) - 1
            while j < k:
                summ = nums[j] + nums[k]
                if summ < target:
                    j += 1
                    continue

                elif summ > target:
                    k -= 1
                    continue

                else:
                    ans.add(tuple([nums[i], nums[j], nums[k]]))
                    j += 1
                    k -= 1

        return list(ans)




        