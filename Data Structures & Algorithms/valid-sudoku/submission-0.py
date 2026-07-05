class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            temp = []
            for j in range(9):
                if board[i][j] in temp and not board[i][j] == ".":
                    print(j)
                    print(i)
                    print(board[i][j])
                    return False
                else:
                    temp += [board[i][j]]
        for i in range(9):
            temp = []
            for j in range(9):
                if board[j][i] in temp and not board[j][i] == ".":
                    print(j)
                    print(i)
                    print(board[j][i])
                    return False
                else:
                    temp += [board[j][i]]
        for i in range(9):
            for j in range(9):
                rowMod = (i + 1) % 3
                colMod = (j + 1) % 3
                if rowMod == 1:
                    selectRows = range(i, i + 3)
                elif rowMod == 2:
                    selectRows = range(i-1, i+2)
                elif rowMod == 0:
                    selectRows = range(i - 2, i+1)
                if colMod == 1:
                    selectCols = range(j, j + 3)
                elif colMod == 2:
                    selectCols = range(j - 1, j + 2)
                elif colMod == 0:
                    selectCols = range(j - 2, j + 1)
                temp = []
                for r in selectRows:
                    for c in selectCols:
                        if board[r][c] in temp and not board[r][c] == ".":
                            print(r)
                            print(c)
                            print(board[r][c])
                            return False
                        else:
                            temp += [board[r][c]]
        return True