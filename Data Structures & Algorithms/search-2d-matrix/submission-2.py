class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1
        index = 0
        while top <= bot:
            row = top + (bot - top) // 2
            index = row
            if target > matrix[row][-1]:
                top = row + 1

            elif target < matrix[row][0]:
                bot = row - 1

            else:
                break

        if top > bot:
            return False

        low, high = 0, cols - 1
        while low <= high:
            mid = low + (high - low) // 2
            if target < matrix[index][mid]:
                high = mid - 1

            elif target > matrix[index][mid]:
                low = mid + 1

            else:
                return True

        return False
        

        