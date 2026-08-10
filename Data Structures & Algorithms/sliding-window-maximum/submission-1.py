class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        running = max(nums[0:k])
        ans = [running]
        left = 0
        for right in range(k, len(nums)):
            if nums[right] > running:
                running = nums[right]

            if nums[left] == running:
                running = max(nums[left + 1: right + 1])

            left += 1
            ans.append(running)

        return ans
        
        