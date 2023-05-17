class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        global temp
        temp = [0]*9
        def validRows(row):
            global temp
            for i in range(9):
                if board[row][i].isnumeric():
                    if temp[int(board[row][i]) - 1] > 0:
                        return False
                    temp[int(board[row][i]) - 1] += 1

            temp = [0] * 9
            return True

        def validCols(cols):
            global temp
            for i in range(9):
                    if board[i][cols].isnumeric():
                        if temp[int(board[i][cols]) - 1] > 0:
                            return False
                        temp[int(board[i][cols]) - 1] += 1
            temp = [0] * 9
            return True


        def validBox(row,col):
            global temp
            for i in range(3):
                if board[row][col + i].isnumeric():
                    if temp[int(board[row][col + i]) - 1] > 0:
                        return False
                    temp[int(board[row][col + i]) -1] += 1
                if board[row + 1][col + i].isnumeric():
                    if temp[int(board[row + 1][col + i]) - 1] > 0:
                        return False
                    temp[int(board[row + 1][col + i]) -1] += 1
                if board[row + 2][col + i].isnumeric():
                    if temp[int(board[row + 2][col + i]) - 1] > 0:
                        return False
                    temp[int(board[row + 2][col + i]) -1] += 1

            temp = [0] * 9
            return True

        for i in range(9):
            if not validRows(i):
                return False
            if not validCols(i):
                return False
        for i in [0,3,6]:
            if not validBox(i,3):
                return False
            if not validBox(i,0):
                return False
            if not validBox(i,6):
                return False
        return True
            
            
        