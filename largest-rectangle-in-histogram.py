# 84. Largest Rectangle in Histogram

'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        n = len(heights)
        tracker = list()
        maxArea = 0
        for i in range(n):
            while(tracker and heights[tracker[-1]] > heights[i]):
                width = i-tracker[-1]
                if len(tracker)>=2:
                    width = width + (tracker[-1]-tracker[-2]-1)
                else:
                    width = width + tracker[-1]
                lastArea = heights[tracker[-1]] * width
                print(lastArea)
                if lastArea > maxArea:
                    maxArea = lastArea
                tracker.pop()
            tracker.append(i)
        return maxArea

'''
Explanation:
Given: An array of integers (heights) representing the histogram's bar height where the width of each bar is 1
Aim: To return the area of the largest rectangle possible

Approach:
- For Each Bar in the Histogram, We need to find how long left and right it can span itself without having to shrink due to a smaller bar
- Append a 0 height at the end to signal the end of the histogram
- Set n as the number of bars in the histogram
- Initiate an empty list tracker through which we'll track the inices of the histogram from left right in a non-decreasing order at any point
- Initialize maxArea as 0
- For every bar in the histogram:
    - While tracker is not empty and the last height put in the tracker is greater than current bar:
        - The last element of tracker can no longer span right as current bar is shorter than it
        - Set width of the tracker[-1] as the width between the current and tracker first covering itself and everything to its right
        - Now add everything that is valid in its left side also to width hence obtaining the whole width tracker[-1] can span across. (All of left if this is the last remaining element in tracker else upto the before element in tracker)
        - If the area covered by rectangle formed by tracker[-1] and width is greater than maxArea, Set maxArea as this area
        - Pop the tracker[-1] and continue while loop as long as conditions satisfy
    - Append current element to tracker
- Return the maxArea calculated
''' 