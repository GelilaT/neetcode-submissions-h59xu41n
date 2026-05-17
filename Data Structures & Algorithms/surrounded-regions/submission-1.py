class Solution:
    def solve(self, board: List[List[str]]) -> None:

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(board), len(board[0])
        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        # visited = [[0 for _ in range(cols)] for _ in range(rows)]
        def dfs(row, col):

            if not inbound(row, col) or board[row][col] != "O":
                return 

            board[row][col] = "T"
            for r, c in directions:
                nr, nc = r + row, c + col
                dfs(nr, nc)

        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols - 1)

        for j in range(cols):
            dfs(0, j)
            dfs(rows - 1, j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "T":
                    board[i][j] = "O"

        

        