#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    return result

if len(sys.argv) < 2:
    print("Please provide an integer argument.")
else:
    try:
        f = factorial(int(sys.argv[1]))
        print(f)
    except ValueError:
        print("Invalid input. Please provide an integer argument.")
