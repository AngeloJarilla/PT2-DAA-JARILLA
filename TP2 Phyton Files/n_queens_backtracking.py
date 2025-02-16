# 4) Backtracking - Simple N-Queens Example
def solve_n_queens(n):
    board = [-1] * n

    def is_safe(row, col):
        for r in range(row):
            if board[r] == col or abs(board[r] - col) == abs(r - row):
                return False
        return True
    
    def backtrack(row):
        if row == n:
            print("Solution:", board)
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)

solve_n_queens(4)
