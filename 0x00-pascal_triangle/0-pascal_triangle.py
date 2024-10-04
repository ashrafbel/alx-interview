#!/usr/bin/python3
"0-pascal_triangle"


def pascal_triangle(n):
    """
    Generates a list of lists containing integers
    that represent Pascal's Triangle.
    """
    if n <= 0:
        return []

    t = []

    for x in range(n):
        r = [1] * (x + 1)

        if x > 1:
            for j in range(1, x):
                r[j] = t[x - 1][j - 1] + t[x - 1][j]

        t.append(r)

    return t
