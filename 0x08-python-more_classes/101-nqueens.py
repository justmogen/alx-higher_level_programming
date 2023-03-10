#!/usr/bin/python3
import sys

# Check if the argument is an integer
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# Check if N is at least 4
if N < 4:
    print("N must be at least 4")
    sys.exit(1)

# Initialize the board as an empty N x N matrix
board = [[0 for x in range(N)] for y in range(N)]

# Check if a queen can be placed in column j, row i
def is_safe(board, i, j):
    # Check if there is a queen in the same row
    for x in range(N):
        if board[i][x] == 1:
            return False
    # Check if there is a queen in the same column
    for x in range(N):
        if board[x][j] == 1:
            return False
    # Check if there is a queen in the same diagonal (from top-left to bottom-right)
    x, y = i, j
    while x >= 0 and y >= 0:
        if board[x][y] == 1:
            return False
        x -= 1
        y -= 1
    x, y = i, j
    while x < N and y < N:
        if board[x][y] == 1:
            return False
        x += 1
        y += 1
    # Check if there is a queen in the same diagonal (from top-right to bottom-left)
    x, y = i, j
    while x >= 0 and y < N:
        if board[x][y] == 1:
            return False
        x -= 1
        y += 1
    x, y = i, j
    while x < N and y >= 0:
        if board[x][y] == 1:
            return False
        x += 1
        y -= 1
    # If all tests pass, the position is safe
    return True

# Recursive function to place queens on the board
def place_queens(board, col):
    # If all queens have been placed, print the board
    if col == N:
        print([ [i, j] for i in range(N) for j in range(N) if board[i][j] == 1 ])
        return
    # Try placing a queen in each row of the current column
    for row in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            place_queens(board, col + 1)
            board[row][col] = 0

# Start the recursive function from the first column
place_queens(board, 0)

