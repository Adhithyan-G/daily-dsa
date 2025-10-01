# 62. Unique Paths

'''
Question:
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
'''

import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m+n-2, m-1)


'''
Explanation:
Given: Two integers m and n representing the dimensions of a grid
Aim: Count how many unique paths exist from top-left (0,0) to bottom-right (m-1,n-1)
Rules: Robot can only move either right or down

Approach:
- To go from start to finish, robot must always move down exactly (m-1) times and right exactly (n-1) times
- That means every valid path is made up of (m+n-2) moves total
- Out of these moves, we just need to decide which ones are "down" (m-1 moves)
- Once the positions of the down moves are chosen, the rest are automatically right moves
- Number of ways to choose (m-1) positions out of (m+n-2) total = (m+n-2)C(m-1)
- Use math.comb to directly calculate this 
- This gives the exact count of unique paths
'''