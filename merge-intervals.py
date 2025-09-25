# 56. Merge Intervals

'''
Question:

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        left, right = -1, -1
        res = list()
        for i in intervals:
            if left == -1:
                left, right = i[0], i[1]
                continue
            if i[0] > right:
                res.append([left, right])
                left = i[0]
            right = i[1] if i[1] > right else right
        res.append([left, right])
        return res

'''
Explanation:
Given: A list of intervals (intervals)
Aim: To merge overlapping intervals and return the final disjoint intervals

Approach:
- Sort the intervals list with respect to to the start of each interval
- Initialize left and right as -1
- Create an empty list (res) which will contain the merged intervals
- For every interval in intervals:
    - If left is -1 (unintialized), Set left as start of current interval and right as end of current interval and skip to next interval
    - If the start of current interval is greater than last interval's right, Then we are starting a new disjoint interval: 
        - Append [left, right] to res as a merged interval upto now and update left to be current interval's start
    - Update right as end of current interval if the end is greater than existing right
- Append last merged interval to res and return res
'''