# Log Parsing Project

This project involves creating a script that reads log lines from standard input (stdin), computes metrics based on the provided log format, and prints statistics after every 10 lines or when interrupted with CTRL + C. The statistics include the total file size and the number of lines by status code.

## Requirements

- Your script should be written in Python 3.
- The script must be executable.
- The script should follow the PEP 8 style guidelines (version 1.7.x).
- All files should end with a newline.
- The first line of your script should be `#!/usr/bin/python3`.
- A `README.md` file at the root of the project folder is mandatory.

## Usage

1. First, run the log generator script to simulate log data. The generator script randomly generates log lines:

    ```bash
    ./0-generator.py | ./0-stats.py
    ```

2. The `0-stats.py` script will read the log lines and print statistics after every 10 lines or when interrupted with CTRL + C.

## Input Format

The expected input format for log lines is as follows:


## Output

The script will print statistics including the total file size and the number of lines by status code (200, 301, 400, 401, 403, 404, 405, and 500). Status codes will be printed in ascending order.

## Example

Here's an example of how the script works:


## Author

This project is implemented by [Aman Brhane].
