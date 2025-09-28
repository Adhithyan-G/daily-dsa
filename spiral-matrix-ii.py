# 59. Spiral Matrix II

'''
Question: 
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
'''

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n==1:
            return [[1]]
        matrix = [[0 for cols in range(n)] for rows in range(n)]
        left, right = 0, n
        up, down = 0, n
        val = 1
        while (left<right):
            for i in range(left, right):
                matrix[up][i] = val
                val=val+1 if right-i != 1 else val
            for i in range(up, down):
                matrix[i][right-1] = val
                val=val+1 if down-i != 1 else val
            for i in range(right-1, left, -1):
                matrix[down-1][i] = val
                val+=1 
            for i in range(down-1, up, -1):
                matrix[i][left] = val
                val+=1
            left+=1
            up+=1
            right-=1
            down-=1
        return matrix

'''
Explanation:
Given: A positive integer n
Aim: To generate an n x n matrix filled with numbers from 1 to n^2 in spiral order

Approach:
- Initialize an n x n matrix with all elements as 0
- Set boundaries: left = 0, right = n, up = 0, down = n
- Start filling values from 1 upwards (val = 1) 
- Loop while left < right:
    - Fill the top row from left to right, incrementing val by 1 except for the last cell as it would be refilled when done for right column
    - Fill the right column from up to down, incrementing val by 1 except for the last cell as it would be refilled when done for bottom row
    - Fill the bottom row from right to left, incrementing val by 1.Here we increment for all elements as we actually won't reach the leftmost cell
    - Fill the right column from up to down, incrementing val by 1.Here we increment for all elements as we actually won't reach the topmost cell
    - Each pass fills one layer of the spiral. We shrink boundaries and move to the next layer
- Return the filled matrix
'''