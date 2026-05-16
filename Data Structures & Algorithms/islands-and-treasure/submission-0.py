class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def bfs(i, j):

            q = deque([[i, j]])
            distance = 0
            visited = [[0 for _ in range(cols)] for _ in range(rows)]
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return distance

                    for x_change, y_change in directions:
                        newX, newY = row + x_change, col + y_change
                        if inbound(newX, newY) and not visited[newX][newY] and grid[newX][newY] != -1:
                            q.append([newX, newY])
                            visited[newX][newY] = 1
                
                distance += 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0 and grid[i][j] != -1:
                    steps = bfs(i, j)
                    grid[i][j] = steps if steps else grid[i][j] 

        # return grid



        
        