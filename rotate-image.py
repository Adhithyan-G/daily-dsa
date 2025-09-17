# 48. Rotate Image

'''
Question:
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        end=len(matrix)-1
        start=0
        while(end>start):
            iter=1
            while iter<=3:
                for i in range(start, end):
                    if iter==1:
                        matrix[start][i], matrix[i][end] = matrix[i][end], matrix[start][i]
                    if iter==2:
                        matrix[start][i], matrix[end][end+start-i] = matrix[end][end+start-i], matrix[start][i]
                    if iter==3:
                        matrix[start][i], matrix[end+start-i][start] = matrix[end+start-i][start], matrix[start][i]
                iter+=1
            start+=1
            end-=1

'''
Explanation: 
Given: A 2D matrix of integers
Aim: To Rotate the Matrix by 90 degrees

Approach:
- We Rotate the matrix Layer by layer, First we put everything in the outer layer at its place then move inside
- Set start as 0 and end as length of dimension of matrix minus 1
- While end is greater than start:
    - Initialize iter as 1, We use this to decide with which side of matrix to swap the top side with
    - We do three sets of swaps, top with each other side:
        - If iter is 1, swap the top and right side of the layer. After Swap, Top has Right
        - If iter is 2, swap the top (actually right) and bottom side of the layer. After Swap, Top has Bottom
        - If iter is 3, swap the top (actually bottom) and left side of the layer. After Swap, Top has Left
        - Increment iter by 1
    - Now the all elements of the current layer are at their respective places, Move on to next layer
    - Increment start by 1 and decrement end by 1
- Finally we have the fully rotated matrix rotated layer by layer. 
- Time Complexity is O(n^2) where every swap puts an element at it desired place and does n^2 swaps
'''