class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binarySearch(left):
            low, high = 0, len(nums) - 1
            middle = -1
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] < target:
                    low = mid + 1

                elif nums[mid] > target:
                    high = mid - 1

                else:
                    middle = mid
                    if left:
                        high = mid - 1
                    else:
                        low = mid + 1

            return middle

        left = binarySearch(True)
        right = binarySearch(False)
        return [left, right]

                

    





        