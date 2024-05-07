#!/usr/bin/python3
import sys

# Description of the function: This function calculates the factorial of a given integer.
def factorial(n):
    # Settings :
     # - n: The integer whose factorial we want to calculate.

    # Returns:
     # - The factorial of n.

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Call the factorial function with the first command line argument.
f = factorial(int(sys.argv[1]))
print(f)
