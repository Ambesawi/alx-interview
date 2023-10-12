#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor
can execute only two operations in this file: `Copy All` and `Paste`.

@TODO:
    Deines a method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    Args:
        n (int): length of letter `H` required in the file
    Returns:
        (int): number of minimum operations if possible otherwise 0
    """
    minimumOperations = 2
    totalOperations = 0
    while n > 1:
        while n % minimumOperations == 0:
            totalOperations += minimumOperations
            n /= minimumOperations
        minimumOperations += 1
    return totalOperations
