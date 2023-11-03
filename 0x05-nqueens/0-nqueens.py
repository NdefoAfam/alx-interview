#!/usr/bin/python3#!/usr/bin/python3
"""N Queens placement on NxN chessboard"""


import sys

def is_safe(board, row, col):
    # Check if a queen can be placed at board[row][col]
    
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens(board, row):
    # Recursively solve the N Queens problem
    if row == len(board):
        # All queens are placed, print the solution
        for r in board:
            print(r)
        print()
        return
    
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens(board, row + 1)
            board[row][col] = 0

def nqueens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    
    N = int(N)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens(board, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    nqueens(sys.argv[1])
