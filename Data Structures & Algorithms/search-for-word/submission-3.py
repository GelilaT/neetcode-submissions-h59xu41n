class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(board), len(board[0])
        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def dfs(row, col, path, visited):

            if "".join(path) == word:
                return True

            if len(path) >= len(word):
                return False

            res = False
            for x, y in directions:
                newRow = row + x
                newCol = col + y

                if inbound(newRow, newCol) and (newRow, newCol) not in visited:
                    visited.add((newRow, newCol))
                    path.append(board[newRow][newCol])
                    res = res or dfs(newRow, newCol, path, visited)
                    visited.remove((newRow, newCol))
                    path.pop()

            return res

        ans = False
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    ans = ans or dfs(i, j, [word[0]], set([(i, j)]))

        return ans

        