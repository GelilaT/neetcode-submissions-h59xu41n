class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def dfs(i, j):

            visited[i][j] = 1
            for x, y in directions:
                newX = i + x
                newY = j + y

                if inbound(newX, newY) and not visited[newX][newY] and grid[newX][newY] == "1":
                    dfs(newX, newY)

        ans = 0
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j] == "1":
                    dfs(i, j)
                    ans += 1

        return ans
