# 74. Search a 2D Matrix

'''
Question:
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        listsize = rows * cols
        left = 0
        right = listsize-1
        while left<=right:
            mid = (left+right)//2
            row = mid//cols
            col = mid%cols
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                left = mid+1
            else:
                right = mid-1
        return False

'''
Explanation:
Given: An m x n matrix sorted in ascending order row-wise, and where each row's first element is greater than the previous row’s last.
Aim: To determine if a target integer exists within the matrix in O(log(m * n)) time.

Approach:
- Treat the matrix as a single flattened sorted list of size (rows x cols).
- Initialize:
    - left = 0
    - right = (rows x cols) - 1
- Perform binary search:
    - Compute mid = (left + right) // 2
    - Convert mid index to 2D indices:
        - row = mid // cols
        - col = mid % cols
    - If matrix[row][col] == target → return True.
    - If value < target → move left pointer to mid + 1.
    - Else → move right pointer to mid - 1.
- If search completes with no match → return False.
'''