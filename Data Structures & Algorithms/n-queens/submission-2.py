class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def inbound(row, col):
            return 0 <= row < n and 0 <= col < n

        def checker(i, j, visited):
            
            # check rows
            for y in range(j):
                if visited[i][y] == 'Q':
                    return False

            # check columns
            for x in range(i):
                if visited[x][j] ==  'Q':
                    return False

            # check diagonals
            x, y = i - 1, j - 1
            while inbound(x, y):
                if visited[x][y] == 'Q':
                    return False

                x, y = x - 1, y - 1

            x, y = i - 1, j + 1
            while inbound(x, y):
                if visited[x][y] == 'Q':
                    return False

                x, y = x - 1, y + 1

            return True

        def dfs(row, visited):
            
            nonlocal ans
            if row >= n:
                ans.append([''.join(row) for row in visited])
                return

            for i in range(n):
                if checker(row, i, visited):
                    visited[row][i] = 'Q'
                    dfs(row + 1, visited)
                    visited[row][i] = '.'

        ans = []
        visited = [['.' for _ in range(n)] for _ in range(n)]
        dfs(0, visited)
        return ans
            
            

        