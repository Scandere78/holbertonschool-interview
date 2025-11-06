#!/usr/bin/python3
"""
Module 0-pascal_triangle
Returns Pascal’s triangle of n
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]  # première ligne

    for i in range(1, n):
        prev_row = triangle[-1]
        # Chaque ligne commence et se termine par 1
        row = [1]

        # Calcul des valeurs intermédiaires
        for j in range(1, len(prev_row)):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle

