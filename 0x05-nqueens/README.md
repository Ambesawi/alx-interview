# N Queens Solver

This project is dedicated to solving the N queens puzzle, a classic problem in which N non-attacking queens must be placed on an N×N chessboard. The project's goal is to find and print every possible solution to this puzzle.

## Table of Contents

- [Introduction](#introduction)
- [Task](#task)
- [Requirements](#requirements)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The N queens puzzle is a well-known problem in the field of computer science and mathematics. It involves placing N queens on an N×N chessboard in a way that no two queens can attack each other. The project aims to find all possible solutions to this puzzle, given the value of N.

## Task

The main task of this project is to implement a Python program that can solve the N queens puzzle for a given N. The program should follow these criteria:

- Accept an integer N as a command-line argument.
- Validate the input:
  - If the user called the program with the wrong number of arguments, print "Usage: nqueens N," followed by a new line, and exit with status 1.
  - Ensure that N is an integer greater than or equal to 4. If not, display appropriate error messages and exit with status 1.
- Find and print every possible solution to the N queens puzzle:
  - Each solution should be presented as a list of coordinates, where each pair (x, y) represents the position of a queen.
  - One solution should be printed per line.

The project also requires adherence to coding style and executable file standards.

## Requirements

- **Operating System and Python Version**:
   - Develop your code on Ubuntu 20.04 LTS using Python 3.4.3.

- **File Format**:
   - Ensure all your code files end with a new line.

- **Shebang Line**:
   - Start all your Python code files with `#!/usr/bin/python3`.

- **README.md File**:
   - Create a `README.md` file at the root of your project folder. This file should provide information about your project, its purpose, and how to use it.

- **Coding Style**:
   - Adhere to the PEP 8 style (version 1.7.*).

- **Executable Files**:
   - Ensure that all your Python files are executable.

## Usage

To use this N Queens Solver, follow these steps:

1. Clone the project repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/n-queens-solver.git
