# 73. Set Matrix Zeroes

'''
Question:
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        coltracker = [1 for _ in range(cols)]
        rowtracker = [1 for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rowtracker[i] = 0
                    coltracker[j] = 0
        for i in range(rows):
            for j in range(cols):
                if rowtracker[i] == 0 or coltracker[j] == 0:
                    matrix[i][j] = 0

'''
Explanation:
Given: An m x n matrix of integers.
Aim: To modify the matrix in place such that if any element is 0, its entire row and column are set to 0.

Approach:
- Determine matrix dimensions as rows and cols.
- Create two trackers:
    - rowtracker of size rows, initialized to 1.
    - coltracker of size cols, initialized to 1.
  These trackers store which rows and columns should be zeroed.

- Traverse the matrix for each element (i, j):
    - If matrix[i][j] == 0:
        - Mark rowtracker[i] = 0
        - Mark coltracker[j] = 0
  This identifies all rows and columns affected by zeros.

- Traverse the matrix again for each element (i, j):
    - If rowtracker[i] == 0 or coltracker[j] == 0:
        - Set matrix[i][j] = 0
  This step applies the zeroing based on identified rows and columns.

- The matrix is modified in place with all necessary zeros applied.
'''
