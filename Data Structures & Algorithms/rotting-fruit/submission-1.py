class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def bfs(row, col):

            q = deque([[row, col]])
            steps = 1
            visited = [[0 for _ in range(cols)] for _ in range(rows)]
            while q:
                n = len(q)
                for _ in range(n):
                    i, j = q.popleft()
                    for x, y in directions:
                        newX, newY = i + x, j + y
                        if inbound(newX, newY) and grid[newX][newY] == 2:
                            return steps

                        if inbound(newX, newY) and not visited[newX][newY] and grid[newX][newY] == 1:
                            visited[newX][newY] = 1
                            q.append([newX, newY])
                
                steps += 1
            
            return -1

        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    step = bfs(i, j)
                    if step == -1:
                        return -1

                    ans = max(step, ans)

        return ans



                    



        