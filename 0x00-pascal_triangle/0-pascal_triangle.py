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

  res = [[1]]
  for i in range(1, n):
    level = [1]
    for j in range(1, i):
      level.append(res[i-1][j-1] + res[i-1][j])
    level.append(1)
    res.append(level)

  return res
