class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        max_area = 0
        def dfs(i, j):

            nonlocal area
            visited[i][j] = 1
            for x, y in directions:
                row = x + i
                col = y + j
                if inbound(row, col) and not visited[row][col] and grid[row][col]:
                    dfs(row, col)
                    area += 1

        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j]:
                    area = 1
                    dfs(i, j)
                    max_area = max(area, max_area)

        return max_area