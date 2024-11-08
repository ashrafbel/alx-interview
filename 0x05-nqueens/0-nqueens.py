#!/usr/bin/python3
"N queens"
import sys


def is_safe(board, row, col, N):
    """
    Check if it is safe to place a queen at position (row, col).
    
    Args:
        board (list): A list representing the positions of queens on the board.
        row (int): The row to place the queen.
        col (int): The column to place the queen.
        N (int): The size of the chessboard.

    Returns:
        bool: True if the position is safe, False otherwise.
    """
    # Check for queens in the same column
    for i in range(row):
        if board[i][1] == col:
            return False

    # Check for queens in the same diagonal
    for i in range(row):
        if abs(board[i][0] - row) == abs(board[i][1] - col):
            return False

    return True


def solve_nqueens(N, board, row):
    """
    Solve the N-Queens puzzle using backtracking.
    
    Args:
        N (int): The size of the chessboard and the number of queens.
        board (list): A list to store the positions of queens.
        row (int): The current row to place the queen.
    
    Returns:
        None
    """
    # If all queens are placed, print the solution
    if row == N:
        print(board)
        return

    # Try placing the queen in all columns of the current row
    for col in range(N):
        if is_safe(board, row, col, N):
            board.append([row, col])  # Place the queen
            solve_nqueens(N, board, row + 1)  # Try placing queens in the next row
            board.pop()  # Backtrack


def nqueens(N):
    """
    Check if the user input is valid and solve the N-Queens puzzle.
    
    Args:
        N (int): The size of the chessboard and the number of queens.
    
    Returns:
        None
    """
    # Check if the correct number of arguments is passed
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

    board = []  # This list will store the positions of queens
    solve_nqueens(N, board, 0)


if __name__ == '__main__':
    """
    Main function to execute the program.
    """
    nqueens(4)  # For testing, you can pass the size of the board, e.g., nqueens(4)

