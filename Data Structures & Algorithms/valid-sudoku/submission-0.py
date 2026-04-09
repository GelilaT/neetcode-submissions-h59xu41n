class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def checkRow(i):

            visited = set()
            for j in range(9):
                if board[i][j] != ".":
                    if int(board[i][j]) in visited:
                        return False

                    visited.add(int(board[i][j]))

            return True

        def checkCol(j):
            
            visited = set()
            for i in range(9):
                if board[i][j] != ".":
                    if int(board[i][j]) in visited:
                        return False

                    visited.add(int(board[i][j]))

            return True

        def checkRec(x, y):

            visited = set()
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    if board[i][j] != ".":
                        if int(board[i][j]) in visited:
                            return False

                        visited.add(int(board[i][j]))
                        
            return True

        for i in range(9):
            if not checkRow(i):
                return False

        for j in range(9):
            if not checkCol(j):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not checkRec(i, j):
                    return False

        return True


        