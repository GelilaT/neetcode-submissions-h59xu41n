class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binarySearch(low, high):

            while low <= high:
                midd = low + (high - low) // 2
                if nums[midd] < target:
                    low = midd + 1
                elif nums[midd] > target:
                    high = midd - 1
                else:
                    return midd

            return -1

        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] < nums[high]:
                high = mid 

            else:
                low = mid + 1

        mid = low
        res = binarySearch(0, mid - 1)
        if res != -1:
            return res
        
        return binarySearch(mid, len(nums) - 1)

        