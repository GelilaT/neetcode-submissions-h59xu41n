class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(heights), len(heights[0])
        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def dfs(i, j, visited):

            visited[i][j] = 1
            for x, y in directions:
                row, col = i + x, j + y

                if inbound(row, col) and not visited[row][col] and heights[row][col] >= heights[i][j]:
                    dfs(row, col, visited)

        visitedP = [[0 for _ in range(cols)] for _ in range(rows)]
        visitedA = [[0 for _ in range(cols)] for _ in range(rows)]
        for j in range(cols):
            dfs(0, j, visitedP)
            dfs(rows - 1, j, visitedA)

        for i in range(rows):
            dfs(i, 0, visitedP)
            dfs(i, cols - 1, visitedA)

        ans = []
        for i in range(rows):
            for j in range(cols):
                if visitedA[i][j] == 1 and visitedP[i][j] == 1:
                    ans.append([i, j])

        return ans



        