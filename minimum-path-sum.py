# 64. Minimum Path Sum

'''
Question:
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        tracker = [0 for _ in range(len(grid[0]))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if j == 0:
                    tracker[j] = tracker[j]+grid[i][j]
                elif i == 0:
                    tracker[j] = grid[i][j]+tracker[j-1]
                else:
                    tracker[j] = min(tracker[j]+grid[i][j], tracker[j-1]+grid[i][j])
        return tracker[-1]

'''
Explanation: 
Given: A (m x n) grid filled with non-negative numbers
Aim: To find a path from top left to bottom right where the sum of all numbers along the path is minimum while moving only down are right.

Approach:
- Initialize a list tracker with n number of 0s where n would be number of columns of the grid.
- For every row in the grid:
    - For every element in the row:
        - If it is the first element of the row, Set tracker of current element index of row (i) as the sum of tracker[i] and current element as this element can only be reached from above element.
        - Else if it is the first row, Populate the initial tracker list with the increasing horizontal sum as each element can be reached only from its left as this is the first row and there are no elements above.
        - Else, Set tracker[i] as the minimum of reaching current element from either the left or the top as we want the path which is of minimal sum.
- Return the last element of tracker which would contain the sum of the minimal path
'''