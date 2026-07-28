class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(matrix), len(matrix[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        def dfs(row, col):

            for i in range(cols):
                if matrix[row][i]:
                    matrix[row][i] = -1

            for j in range(rows):
                if matrix[j][col]:
                    matrix[j][col] = -1

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    dfs(i, j)

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0              
            

        