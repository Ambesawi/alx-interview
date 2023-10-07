# Lockboxes Project

## Overview

In this project, you will implement a Python function to solve the "Lockboxes" problem. The problem involves determining whether all the boxes can be opened, where each box may contain keys to other boxes. This project will help you practice Python programming and problem-solving skills.

## Requirements

### General

- **Allowed Editors**: You are allowed to use vi, vim, or emacs for coding.
- **Python Version**: All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3).
- **File Endings**: Ensure that all your files end with a newline character.
- **Shebang Line**: The first line of all your Python files should be exactly `#!/usr/bin/python3`.
- **README.md**: A mandatory README.md file must be present at the root of your project folder.
- **Code Documentation**: Your code should be well-documented.
- **Code Style**: Follow the PEP 8 style guidelines (version 1.7.x).
- **Executable Files**: All your Python files must be executable.

### Task Description

**0. Lockboxes**

Write a Python function `canUnlockAll(boxes)` that takes a list of lists as input. Each inner list represents a box, and each box may contain keys to other boxes. The function should determine if all the boxes can be opened.

- A key with the same number as a box opens that box.
- You can assume all keys will be positive integers.
- There can be keys that do not have boxes.
- The first box `boxes[0]` is unlocked.

**Function Prototype**:

```python
def canUnlockAll(boxes)

