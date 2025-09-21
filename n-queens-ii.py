# N-Queens II

'''
Question: 
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.
'''

class Solution:
    def totalNQueens(self, n: int) -> int:
        colcomp = set()
        dia1comp = set()
        dia2comp = set()
        res = 0
        def recursivePlaceQueens(row):
            if row == n:
                nonlocal res
                res+=1
                return
            for i in range(0,n):
                if i not in colcomp and (i-row) not in dia1comp and (i+row) not in dia2comp:
                    colcomp.add(i)
                    dia1comp.add(i-row)
                    dia2comp.add(i+row)
                    recursivePlaceQueens(row+1)
                    colcomp.remove(i)
                    dia1comp.remove(i-row)
                    dia2comp.remove(i+row)
        recursivePlaceQueens(0)
        return res
            
'''
Explanation: 
Given: A integer (n) used to signify a nxn chess board
Aim: To find all placement combinations of n Queens in the board such that no queen can attack each other

Approach:
- Initialize empty sets that indicate covered column (colcomp), Left-Up to Right-Down Diagonal (dia1comp), Right-Up to Left-Down Diagonal (dia2comp)
- Initialize an integer to track count of all possible combinations as 0(res)
- Define Recursive function (recursivePlaceQueens) which takes in the row index as argument:
    - If row is equal to n, It signifies that n queens were placed at positions non-hostile to each other. Increment res by 1 (Required to declare res as nonlocal as integers are immutable)
    - For every column (i) in the row:
        - Check Whether current position conflicts with any other queen by checking the column, And two diagonals 
        - Note: For one diagonal of the Chess board, the difference between the row and column always remains same. And for the other diagonal their sum always remains same. Hence we check those for diagonals
        - If non-conflicting:
            - Add i to colcomp, i-row to dia1comp and i+row to dia2comp
            - Call recursivePlaceQueens for next row
            - After the recursive function has completely explored its branch and returned back here, Undo the additions to colcomp, dia1comp, dia2comp in order to clear up the state for the next column in same row as having it stay here would conflict with the row rule
- Initiate recursivePlaceQueens with row as 0
- Return res that would contain count of all possible positioning combinations
'''