#!/usr/bin/python3#!/usr/bin/python3
"""N Queens placement on NxN chessboard"""


import sys

def nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    def is_safe(board, row, col):
        for r, c in board:
            if r == row or c == col or r + c == row + col or r - c == row - col:
                return False
        return True
    def backtrack(board, row):
        if row == n:
            print(board)
            return
        for col in range(n):
            if is_safe(board, row, col):
                board.append([row, col])
                backtrack(board, row + 1)
                board.pop()
    backtrack([], 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    nqueens(n)
