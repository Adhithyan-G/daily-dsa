# 54. Spiral Matrix

'''
Question: 
Given an m x n matrix, return all elements of the matrix in spiral order.
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows=len(matrix)
        cols=len(matrix[0])
        up, left = 0, 0
        down, right = rows-1, cols-1
        res=list()
        while(up<=down and left<=right):
            for i in range(left, right+1):
                res.append(matrix[up][i])
            up+=1
            for i in range(up,down+1):
                res.append(matrix[i][right])
            right-=1
            if up>down or right<left:
                break
            for i in range(right, left-1, -1):
                res.append(matrix[down][i])
            down-=1
            for i in range(down, up-1, -1):
                res.append(matrix[i][left])
            left+=1
        return res

'''
Explanation: 
Given: A 2D integer matrix
Aim: To return all elements of the matrix in spiral order

Approach: 
- Spiral order starting from [0,0] of the matrix goes all the way right until it hits the last non-encountered element then down for the same, then left then up and repeats until all elements have been covered
- We set rows as number of rows, the number of lists in the matrix that represent rows
- We set cols as number of columns, the number elements in each list of the matrix
- Initiate up and left as 0, indicating the first row and first column respectively
- Initiate down and right as rows-1 and cols-1, indicating the last row and last column respectively
- Initiate res as an empty list which will finally contain the elements in the spiral order
- Loop as long as up is less than or equal to down and left is less than or equal to right (If any of these conditions break it means the matrix is fully processed):
    - Append all elements to res in the up row from left to right and then increment up by 1 (move up downward, as all elements in up row are done)
    - Append all elements to res in the right column from up to down and decrement right by 1 (move right leftward, as all elements in right column are done)
    - Check that the matrix bounded by up, down, left, right is still valid by ensuring up is not greater than down and right is not lesser than left. If Invalid, Exit loop as it indicates the matrix has been fully processed. 
    - Append all elements to res in the down row from right to left and then decrement down by 1 (move down upward, as all elements in down row are done)
    - Append all elements to res in the left column from down to up and increment left by 1 (move left rightward, as all elements in left column are done)
    - Every iteration peels off the outer layer of the matrix
- Return res

- Each element is visited exactly once and hence time complexity is O(mn)
'''