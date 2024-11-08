#!/usr/bin/python3
"N queens"
import sys


def is_safe(board, row, col, N):
    """
    Check if it is safe to place a queen at position (row, col).
    """
    for i in range(row):
        if board[i][1] == col:
            return False
    for i in range(row):
        if abs(board[i][0] - row) == abs(board[i][1] - col):
            return False
    return True


def solve_nqueens(N, board, row):
    """
    Solve the N-Queens puzzle using backtracking.
    """
    if row == N:
        print(board)
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board.append([row, col])
            solve_nqueens(N, board, row + 1)
            board.pop()


def nqueens(N):
    """
    Check if the user input is valid and solve the N-Queens puzzle.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = []
    solve_nqueens(N, board, 0)


if __name__ == '__main__':
    """
    Main function
    """
    nqueens(4)
