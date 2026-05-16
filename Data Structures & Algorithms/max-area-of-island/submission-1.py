class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def dfs(row, col):

            nonlocal area
            visited[row][col] = 1
            for x_change, y_change in directions:
                newX = row + x_change
                newY = col + y_change

                if inbound(newX, newY) and not visited[newX][newY] and grid[newX][newY]:
                    dfs(newX, newY)
                    area += 1

        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j]:
                    area = 1
                    dfs(i, j)
                    max_area = max(area, max_area)

        return max_area

        

        

        


        