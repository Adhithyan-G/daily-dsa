# 85. Maximal Rectangle

'''
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
'''

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0 for _ in range(cols)]
        maxRect = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "0":
                    heights[j] = 0
                else:
                    heights[j] += 1
            heights.append(0)
            tracker = list()
            for i in range(cols+1):
                while(tracker and heights[tracker[-1]] > heights[i]):
                    width = i-tracker[-1]
                    if len(tracker)>=2:
                        width = width + (tracker[-1]-tracker[-2]-1)
                    else:
                        width = width + tracker[-1]
                    lastArea = heights[tracker[-1]] * width
                    if lastArea > maxRect:
                        maxRect = lastArea
                    tracker.pop()
                tracker.append(i)
            heights.pop()
        return maxRect
        
'''
Explanation:
Given: A binary matrix filled with 0's and 1's
Aim: To return the area of the largest rectangle only 1s possible

Approach:

- Treat each row of the matrix as the base of a histogram.
- For each row:
    - For each column, maintain a running height counter representing how many consecutive '1's appear vertically up to that row.
        - If matrix[i][j] == '1', increment heights[j] by 1.
        - If matrix[i][j] == '0', reset heights[j] to 0 since the vertical streak is broken.
    - After processing a row, we now have a histogram representing continuous stacked 1's from current row.
    - Append 0 to mark end of heights
    - Initialize an empty list tracker
    - For every height in the heights:
        - While tracker is not empty and the last height put in the tracker is greater than current bar:
            - The last element of tracker can no longer span right as current bar is shorter than it
            - Set width of the tracker[-1] as the width between the current and tracker first covering itself and everything to its right
            - Now add everything that is valid in its left side also to width hence obtaining the whole width tracker[-1] can span across. (All of left if this is the last remaining element in tracker else upto the before element in tracker)
            - If the area covered by rectangle formed by tracker[-1] and width is greater than maxRect, Set maxRect as this area
            - Pop the tracker[-1] and continue while loop as long as conditions satisfy
        - Append current element to tracker
    - Pop the appended 0 for the next run
- Return the maxRect calculated
''' 