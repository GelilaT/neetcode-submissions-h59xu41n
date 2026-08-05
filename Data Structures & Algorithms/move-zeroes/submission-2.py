class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left, right = 0, 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                left = i
                break

        for i in range(n):
            if nums[i] != 0:
                right = i
                break

        if nums[left] != 0 or nums[right] == 0:
            return nums

        while left < n and right < n:
            
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
                while right < n and nums[right] == 0:
                    right += 1

                while left < n and nums[left] != 0:
                    left += 1

                continue

            right += 1
            while right < n and nums[right] == 0:
                right += 1


        return nums

        