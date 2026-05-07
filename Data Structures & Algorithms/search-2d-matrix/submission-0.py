class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, cols = len(matrix), len(matrix[0])
        index = -1
        for i in range(rows):
            if matrix[i][0] == target or matrix[i][cols - 1] == target:
                return True

            if matrix[i][0] <= target <= matrix[i][cols - 1]:
                index = i
                break

        if index == -1:
            return False

        low, high = 0, cols - 1
        while low <= high:
            mid = low + (high - low) // 2
            if matrix[index][mid] < target:
                low = mid + 1

            elif matrix[index][mid] > target:
                high = mid - 1

            else:
                return True

        return False
        