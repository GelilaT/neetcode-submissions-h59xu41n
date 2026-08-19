class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binarySearch():

            low, high = 0, len(nums) - 1
            while low < high:
                mid = low + (high - low) // 2
                if nums[mid] > nums[high]:
                    low = mid + 1

                else:
                    high = mid

            return low

        index = binarySearch()
        if nums[index] == target:
            return index

        elif nums[index] < target <= nums[-1]:
            low, high = index, len(nums) - 1

        else:
            low, high = 0, index

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return -1




