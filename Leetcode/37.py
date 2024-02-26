def can_place(row, col, c, board):

    if c in board[row]: return False
    if c in [row[col] for row in board]: return False

    brs = 3 * (row // 3)
    bre = brs + 3

    bcs = 3 * (col // 3)
    bce = bcs + 3

    for i in range(brs, bre):
        for j in range(bcs, bce):
            if board[i][j] == c: return False
    return True

def recur(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == ".":
                for c in "123456789":
                    if (can_place(row, col, c, board)):
                        board[row][col] = c
                        if (recur(board)): return True
                        board[row][col] = "."
                return False
    return True

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print(recur(board))
