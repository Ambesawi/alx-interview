#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard.

TODO:
    * Write a program that solves the N queens problem.
"""


def queens(chessBoard, row, majestyz, resolve):
    """
    Args:
        chessBoard (list)
        row (int)
        majestyz (int)
        resolve (list)

    Returns:
        resolve (list)
    """
    if majestyz == len(chessBoard):
        resolve.append(extract(chessBoard))
        return (resolve)

    for col in range(len(chessBoard)):
        if chessBoard[row][col] == -1:
            demo = copyBoard(chessBoard)
            demo[row][col] = 1
            cancel(demo, row, col)
            resolve = queens(demo, row + 1, majestyz + 1, resolve)
    return (resolve)


def cancel(chessBoard, row, col):
    """
    Cancels out vulnerable positions for the queen

    Args:
        chessBoard (list)
        row (int)
        col (int)
    """
    length = len(chessBoard)
    """Cancel forward positions"""
    for c in range(col + 1, length):
        chessBoard[row][c] = 0
    """Cancel backwards positions"""
    for c in range(col - 1, -1, -1):
        chessBoard[row][c] = 0
    """Cancel down positions"""
    for r in range(row + 1, length):
        chessBoard[r][col] = 0
    """Cancel up positions"""
    for r in range(row - 1, -1, 1):
        chessBoard[r][col] = 0
    """Cancel right downward diagonal positions"""
    c = col + 1
    for r in range(row + 1, length):
        if c >= length:
            break
        chessBoard[r][c] = 0
        c += 1
    """Cancel left upward diagonal positions"""
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        chessBoard[r][c] = 0
        c -= 1
    """Cancel right upward diagonal positions"""
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= length:
            break
        chessBoard[r][c] = 0
        c += 1
    """Cancel left downward diagonal positions"""
    c = col - 1
    for r in range(row + 1, length):
        if c < 0:
            break
        chessBoard[r][c] = 0
        c -= 1


def chessBoard(N):
    """
    Create a board of size N * N
    """
    chessBoard = []

    """Create rows"""
    for row in range(N):
        chessBoard.append([])

    """Create columns"""
    for row in chessBoard:
        for n in range(N):
            row.append(-1)

    return (chessBoard)


def copyBoard(chessBoard):
    """
    make a copy of chessBoard
    """
    if type(chessBoard) == list:
        """Recursively copy"""
        return list(map(copyBoard, chessBoard))
    return (chessBoard)


def extract(chessBoard):
    """
    Extract the required outcome from the chess board
    """
    outcome = []
    for row in range(len(chessBoard)):
        for col in range(len(chessBoard)):
            if chessBoard[row][col] == 1:
                outcome.append([row, col])
                break
    return (outcome)


def execute():
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isnumeric() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chess = chessBoard(int(sys.argv[1]))
    resultMatrix = queens(chess, 0, 0, [])
    for row in resultMatrix:
        print(row)


if __name__ == '__main__':
    execute()
