#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
        Compute the factorial of a non-negative integer using recursion.

    Parameters:
        n (int): Non-negative integer whose factorial will be computed.

    Returns:
        int: The factorial of n (n!).
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)
