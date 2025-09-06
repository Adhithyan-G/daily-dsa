# 37. Sudoku Solver
'''
Question:
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
'''

def fillBoard(board, rowid, colid, rows, cols, boxes):
    if rowid == 9:
        return True
    boxid = (rowid//3)*3 + (colid//3)
    if board[rowid][colid] == ".":
        for i in map(str, range(1, 10)):
            if i not in rows[rowid] and i not in cols[colid] and i not in boxes[boxid]:
                board[rowid][colid] = i
                rows[rowid].add(i)
                cols[colid].add(i)
                boxes[boxid].add(i)
                if fillBoard(board, rowid + (colid+1)//9, (colid+1)%9, rows, cols, boxes):
                    return True
                rows[rowid].remove(i)
                cols[colid].remove(i)
                boxes[boxid].remove(i)
        board[rowid][colid] = "."
        return False
    return fillBoard(board, rowid + (colid+1)//9, (colid+1)%9, rows, cols, boxes)


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    val = board[i][j]
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i // 3) * 3 + (j // 3)].add(val)

        fillBoard(board, 0, 0, rows, cols, boxes)

'''
Explanation: 
Given: An incomplete Sudoku Board that HAS a solution as a 2D list
Aim: To fill the Sudoku board to get a valid solution

Approach:

- We need to keep track of what numbers already exist in each row, each column, and each 3x3 box
- We make 3 lists:
    - rows → 9 sets, one for each row
    - cols → 9 sets, one for each column
    - boxes → 9 sets, one for each 3x3 box
- Fill these sets at the start with whatever numbers are already on the board

- Define a recursive function fillBoard that will go cell by cell:
    - If rowid == 9, it means we finished filling the board so return True
    - If the current cell is "." that is empty, we try digits 1–9:
        - For each digit, check if it’s not in the current row, current column, and current box
        - If valid, place it on the board and add it into the corresponding sets
        - Recursively go to the next cell
            - If recursion succeeds, It only will when the board is completed. If yes return True to the parent call
            - Otherwise, revert value to "." and remove from sets and try the next digit
        - If the for loop did not return True, then we have an issue from the parent value filling itself.
    - If the cell is not ".", skip to the next one

- In the main function:
    - Initialize rows, cols, boxes sets with the given numbers
    - Call fillBoard starting from the top-left
'''