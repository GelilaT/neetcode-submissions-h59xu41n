class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def bfs(i, j):

            q = deque([(i, j)])
            visited = [[0 for _ in range(cols)] for _ in range(rows)]
            steps = 0
            while q:

                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 2:
                        return steps

                    for x, y in directions:
                        newX, newY = x + row, y + col
                        if inbound(newX, newY) and not visited[newX][newY] and grid[newX][newY]:
                            q.append((newX, newY))
                            visited[newX][newY] = 1

                steps += 1

        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    steps = bfs(i, j)
                    if not steps:
                        return -1
                    res = max(res, steps)

        return res



        