# 79. Word Search

'''
Question:
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        wordlen = len(word)
        m = len(board)
        n = len(board[0])
        boardChars = dict()
        for i in range(m):
            for j in range(n):
                if board[i][j] not in boardChars:
                    boardChars[board[i][j]] = 0
                boardChars[board[i][j]] += 1
        for c in word:
            if c in boardChars and boardChars[c] != 0:
                boardChars[c] -= 1
            else:
                return False
        def checkfromstart(row,col,index):
            if row < 0 or col < 0 or row >= m or col >= n :
                return False
            if board[row][col] == word[index]:
                board[row][col] = board[row][col] + '.'
                if (index == wordlen-1):
                    return True
                if (checkfromstart(row-1,col,index+1)):
                    return True
                if (checkfromstart(row+1,col,index+1)):
                    return True
                if (checkfromstart(row,col-1,index+1)):
                    return True
                if (checkfromstart(row,col+1,index+1)):
                    return True
                board[row][col] = board[row][col][0]
            return False
        for i in range(m):
            for j in range(n):
                if (checkfromstart(i,j,0)):
                    return True
        return False

'''
Explanation:
Given: An m x n grid of characters board and a string word.
Aim: To determine if the word can be formed by sequentially adjacent cells (horizontally or vertically) without reusing the same cell twice.

Approach:
- Create a dictionary boardChars to store the count of all characters in the board.
- For each character in the word:
    - If that character (key) exists in boardChars and its count is not zero:
        - Decrease its count by one.
    - Else:
        - Return False immediately as the board doesn’t have enough characters to form the word.
- Define a recursive function checkfromstart(row, col, index):
    - If row or col is out of bounds, return False.
    - If board[row][col] matches word[index]:
        - Temporarily mark the cell as visited by appending '.' to it.
        - If index == wordlen - 1:
            - We’ve found all characters successfully, return True.
        - Recursively explore four directions:
            - Up -> checkfromstart(row-1, col, index+1)
            - Down -> checkfromstart(row+1, col, index+1)
            - Left -> checkfromstart(row, col-1, index+1)
            - Right -> checkfromstart(row, col+1, index+1)
        - If none of these return True, backtrack by restoring the cell (remove '.').
    - Return False if mismatch occurs.
- Iterate through every cell (i, j) in the board:
    - If checkfromstart(i, j, 0) returns True, return True as the word exists.
- If no valid path found after exploring all cells, return False.
'''