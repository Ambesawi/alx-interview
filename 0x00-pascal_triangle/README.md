# Pascal's Triangle Generator

## Overview

This Python project includes a function `pascal_triangle(n)` that generates Pascal's Triangle for a specified number of rows, `n`. Pascal's Triangle is a mathematical pattern where each number is the sum of the two numbers directly above it. The function adheres to the following requirements:

- If `n` is less than or equal to 0, the function returns an empty list.
- The input `n` is assumed to always be an integer.

## Usage

To use the `pascal_triangle` function:

1. Import it from the `pascal_triangle` module.
2. Call the function with the desired number of rows (`n`) as an argument.
3. The function will return Pascal's Triangle as a list of lists.

## Example

```python
from pascal_triangle import pascal_triangle

# Example: Generate Pascal's Triangle with 5 rows
triangle = pascal_triangle(5)
print(triangle)

## Output:

[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]

