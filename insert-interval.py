# 57. Insert Interval

'''
Question:

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.
'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newIntervals = list()
        left, right = newInterval[0], newInterval[1]
        if not intervals:
            return [newInterval]
        if left > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals
        if right < intervals[0][0]:
            newIntervals.append(newInterval)
        enc = False
        for i in range(len(intervals)):
            if (newInterval[0] <= intervals[i][0] <= newInterval[1]) or (newInterval[0] <= intervals[i][1] <= newInterval[1]):
                enc = True
                left = intervals[i][0] if intervals[i][0] <= left else left
                right = intervals[i][1] if intervals[i][1] >= newInterval[1] else newInterval[1]
                continue
            if enc:
                newIntervals.append([left,right])
                enc = False
            elif newInterval[0] > intervals[i-1][1] and newInterval[1] < intervals[i][0]:
                newIntervals.append(newInterval)
            newIntervals.append(intervals[i])
        if enc:
            newIntervals.append([left,right])
        return newIntervals

'''
Explanation:
Given: A list of intervals (intervals) sorted in ascending order by start time, and a new interval (newInterval)
Aim: To insert the new interval into intervals such that the result is still sorted and non-overlapping (merging if necessary)

Approach:
- Initialize newIntervals as an empty list which will store the final result
- Extract left and right from newInterval (start and end of the new interval)
- Handle edge cases:
    - If empty list, return list containing newInterval
    - If newInterval starts after the last interval ends, append newInterval at the end and return intervals
    - If newInterval ends before the first interval starts, place newInterval at the beginning of newIntervals
- Initialize enc (a flag) as False, which will track whether we are currently inside an overlapping region
- For every interval in intervals:
    - If the current interval overlaps with newInterval (its start or end lies inside newInterval’s range):
        - Set enc to True
        - Update left to be the minimum of left and the interval’s start
        - Update right to be the maximum of right and newInterval’s end (or the interval’s end if it extends further)
        - Skip appending the current interval since it is merged into newInterval
    - Otherwise (no overlap):
        - If enc is True (we just finished merging), append [left, right] to newIntervals and reset enc
        - Else if the newInterval was disjoint between current interval and last one, append newInterval before appending current
        - Append the current interval directly
- After the loop, if enc is still True (meaning we ended in the middle of a merged block), append [left, right]
- Return newIntervals
'''
