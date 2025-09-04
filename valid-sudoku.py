# 36. Valid Sudoku

'''
Question: 
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        horidicts=list(dict() for i in range(9))
        vertdicts=list(dict() for i in range(9))
        boxdicts=list(dict() for i in range(9))
        boxindex=0
        for i in range(9):
            boxindex=((i//3)*3)
            for j in range(9):
                val=board[i][j]
                if val == ".":
                    continue
                curbox=(boxindex+(j//3))
                if val in vertdicts[j] or val in horidicts[i] or val in boxdicts[curbox]:
                    return False
                vertdicts[j][val] = 1
                horidicts[i][val] = 1
                boxdicts[curbox][val] = 1
        return True        

'''
Explanation: 
Given: A state of a sudoku box filled partially or completely
Aim: To evaluate if the current state is valid, doesn't have to be finishable

Approach: 
- So the rules given in the question should always be satisfied
- Create 3 lists of 9 dictionaries each list denoting a type of group and each dictionary denoting a set of elements of that particular group:
    - horidicts depict horizontal lines and every dictionary in it depicts a horizontal line
    - vertdicts depict vertical lines and every dictionary in it depicts a vertical line
    - boxdicts depict boxes and every dictionary in it depicts a box
- Set boxindex as 0 which changes with the horizontal line's position
- For every position of horizontal line (i):
    - Update boxindex to the product of floor quotient of i and 3
    - For every position of elements in a horizontal line (j) (also denotes every different vertical):
        - Get value of the position and store in val
        - If val is not a number, continue on to next position
        - Find what current box element is in by adding up boxindex and floor quotient of current vertical index
        - If val exists in any of its respective dictionaries, Return False as no duplicates are followed
        - Append value to each of its respective dictionary
- Return True as no duplicates were encountered
'''