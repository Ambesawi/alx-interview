# Rotate 2D Matrix

This project focuses on rotating an n x n 2D matrix 90 degrees clockwise. The rotation is performed in-place without using any external modules.

## Requirements

### General
- Allowed editors: vi, vim, emacs.
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.10.
- All files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/python3`.
- A README.md file at the root of the folder is mandatory.
- Code should adhere to the pycodestyle style (version 2.8.0).
- You are not allowed to import any module.
- All modules and functions must be documented.
- All files must be executable.

## Task

### Rotate 2D Matrix

#### Prototype:
```python
def rotate_2d_matrix(matrix):
 matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate_2d_matrix(matrix)
print(matrix)
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]

