class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        atlantic = [[False] * cols for _ in range(rows)]
        pacific = [[False] * cols for _ in range(rows)]

        for i in range(rows):
            pacific[i][0] = True
            atlantic[i][cols - 1] = True

        for j in range(cols):
            pacific[0][j] = True
            atlantic[rows - 1][j] = True

        def inbound(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs(row, col, path, visited):

            if path[row][col]:
                return True

            visited[row][col] = True

            for dx, dy in directions:
                nr, nc = row + dx, col + dy

                if (
                    inbound(nr, nc)
                    and not visited[nr][nc]
                    and heights[row][col] >= heights[nr][nc]
                ):
                    if dfs(nr, nc, path, visited):
                        path[row][col] = True
                        return True

            return False

        ans = []

        for i in range(rows):
            for j in range(cols):

                visitedAtl = [[False] * cols for _ in range(rows)]
                visitedPac = [[False] * cols for _ in range(rows)]

                atl = dfs(i, j, atlantic, visitedAtl)
                pac = dfs(i, j, pacific, visitedPac)

                if atl and pac:
                    ans.append([i, j])

        return ans