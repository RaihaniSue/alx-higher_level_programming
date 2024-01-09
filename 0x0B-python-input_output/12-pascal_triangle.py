#!/usr/bin/python3
"""Pascal's Triangle Module.
Generates Pascal's triangle of size 'n' as a list of lists of integers.
"""


def pascal_triangle(n):
    """Generates Pascal's triangle of size 'n'.
    Args:
        - n: Size of the triangle (number of rows)
    Returns:
        A list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []

    lis_t = [[0 for x in range(k + 1)] for k in range(n)]
    lis_t[0] = [1]

    for k in range(1, n):
        lis_t[k][0] = 1
        for j in range(1, k + 1):
            if j < len(lis_t[k - 1]):
                lis_t[k][j] = lis_t[k - 1][j - 1] + lis_t[k - 1][j]
            else:
                lis_t[k][j] = lis_t[k - 1][0]
    return lis_t
