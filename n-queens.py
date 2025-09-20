# 51. N-Queens

'''
Question: 
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
'''

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colcomp = set()
        dia1comp = set()
        dia2comp = set()
        poscomp = list()
        res = list()
        def recursivePlaceQueens(row):
            if row == n:
                res.append(poscomp.copy())
                return
            for i in range(0,n):
                if i not in colcomp and (i-row) not in dia1comp and (i+row) not in dia2comp:
                    colcomp.add(i)
                    dia1comp.add(i-row)
                    dia2comp.add(i+row)
                    poscomp.append("."*i + "Q" + "."*(n-1-i))
                    recursivePlaceQueens(row+1)
                    poscomp.pop()
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
- Initialize empty lists to track the Queen positions (poscomp) and to track all possible combinations (res)
- Define Recursive function (recursivePlaceQueens) which takes in the row index as arguement:
    - If row is equal to n, It signifies that n queens were placed at positions non-hostile to each other. Append copy of poscomp (As We edit poscomp in place and not appending a copy would end in empty list at the end) to res and return
    - For every column (i) in the row:
        - Check Whether current position conflicts with any other queen by checking the column, And two diagonals 
        - Note: For one diagonal of the Chess board, the difference between the row and column always remains same. And for the other diagonal their sum always remains same. Hence we check those for diagonals
        - If non-conflicting:
            - Add i to colcomp, i-row to dia1comp and i+row to dia2comp
            - Append String signifying location of queen placed in ith location and index of the string in poscomp would sigify its row position
            - Call recursivePlaceQueens for next row
            - After the recursive function has completely explored its branch and returned back here, Undo the additions to colcomp, dia1comp, dia2comp and poscomp in order to clear up the state for the next column in same row as having it stay here would conflict with the row rule
- Initiate recursivePlaceQueens with row as 0
- Return res that would contain all posible positioning combinations
'''