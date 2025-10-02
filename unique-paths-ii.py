# 63. Unique Paths II

'''
Question: 
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        tracker = [0 for i in obstacleGrid[0]]
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            tracker[0] = 1
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    tracker[j] = 0
                elif j != 0:
                    tracker[j] = tracker[j] + tracker[j-1]
        return tracker[-1]

'''
Explanation:
Given: m x n grid with obstacles marked as 1 and free spaces as 0
Aim: Count number of unique paths from top-left to bottom-right without crossing obstacles

Approach:
- Initialize a tracker array of size n (same as number of columns) with all zeros
- If the starting cell itself is blocked → directly return 0
- Set tracker[0] = 1 to mark that the start position is reachable
- Iterate over every cell in the grid row by row:
    - If current cell is an obstacle, set tracker[j] as 0 (no path through this cell)
    - Otherwise:
        - If j > 0, add number of paths from the left and top → tracker[j] = tracker[j] + tracker[j-1]
        - If j == 0, keep tracker[j] as is (only comes from top)
- After processing entire grid, tracker[-1] will hold number of unique paths to bottom-right
- Using 1D array instead of 2D DP saves space while keeping O(m*n) time
'''