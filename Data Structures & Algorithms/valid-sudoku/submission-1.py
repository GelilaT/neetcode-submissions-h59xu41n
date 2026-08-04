class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def checker(x, y):

            cur = set()
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    if board[i][j] == ".":
                        continue

                    if board[i][j] in cur:
                        return False

                    cur.add(board[i][j])

            return True
        
        def checkRow(i):

            cur = set()        
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if board[i][j] in cur:
                    return False

                cur.add(board[i][j])

            return True
            
        def checkCol(i):

            cur = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue

                if board[j][i] in cur:
                    return False

                cur.add(board[j][i])  

            return True

        for i in range(9):
            if not checkRow(i) or not checkCol(i):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not checker(i, j):
                    return False


        return True




        