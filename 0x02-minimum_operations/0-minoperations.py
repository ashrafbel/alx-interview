#!/usr/bin/python3
"Minimum Operations"


def minOperations(n):
    """
    Calculate the minimum operations to achieve n 'H' characters using
    'Copy All' and 'Paste'.

    Parameters:
    n (int): Target number of 'H' characters.

    Returns:
    int: Minimum operations to reach n 'H' characters; returns 0 if n <= 1.
    """
    if n <= 1:
        return 0
    o = 0
    f = 2
    while n > 1:
        if n % f == 0:
            o += f
            n //= f
        else:
            f += 1
    return o
