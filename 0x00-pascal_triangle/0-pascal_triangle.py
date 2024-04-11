#!/usr/bin/python3
"""
0. Pascal's Triangle
"""

def pascal_triangle(n):
  """
  Create a function def pascal_triangle(n): that returns a list of lists
  of integers representing the Pascal's triangle of n rows.

  Args:
      n: The number of rows in the Pascal's triangle.

  Returns:
      A list of lists representing the Pascal's triangle.
  """

  if n <= 0:
    return []

  res = [[1]]  # Base case: first row is always [1]

  for i in range(1, n):
    level = [1]  # Start each row with 1
    for j in range(1, i):
      # Utilize previous calculations from the same row
      level.append(res[i-1][j-1] + res[i-1][j])
    level.append(1)  # End each row with 1
    res.append(level)

  return res
