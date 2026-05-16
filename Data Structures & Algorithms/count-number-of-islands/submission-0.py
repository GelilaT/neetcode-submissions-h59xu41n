class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        def dfs(row, col):

            visited[row][col] = 1
            for x_change, y_change in directions:
                newX = row + x_change
                newY = col + y_change

                if inbound(newX, newY) and not visited[newX][newY] and grid[newX][newY] == "1":
                    dfs(newX, newY)

        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i, j)
                    islands += 1

        return islands


                

        