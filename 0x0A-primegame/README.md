# 0x0A. Prime Game

## Overview

Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

This project involves implementing a function to determine the winner of each game after playing x rounds. Assuming Maria always goes first and both players play optimally, the function `isWinner` should return the name of the player that won the most rounds. If the winner cannot be determined, it should return `None`.

## Function Prototype

```python
def isWinner(x, nums):
    """
    Determine the winner of each game.

    Args:
    - x: Number of rounds
    - nums: Array of n for each round

    Returns:
    - Name of the player that won the most rounds
    - None if the winner cannot be determined
    """
    # Your implementation here


from 0-prime_game import isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))


./main_0.py

