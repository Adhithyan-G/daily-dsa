# 90. Subsets II

'''
Question:
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = list()
        n = len(nums)
        track = list()
        def findsubs(tracker,index):
            for i in range(index, n):
                if i != index and nums[i] == nums[i-1]:
                    continue
                tracker.append(nums[i])
                findsubs(tracker, i+1)
                tracker.pop()
            subsets.append(tracker.copy())
        findsubs(track, 0)
        return subsets

'''
Explanation:
Given: A list (nums) which may have duplicates.
Aim: To Generate all unique subsets of nums.

Approach:
- Set n as length of nums.
- Maintain:
        - track -> That tracks the current subset being created
        - subsets -> list to store all complete subsets
- Define a recursive function findsubs(tracker, index):
    - For every i from index to n:
        - If i is not index but is equal to the the last element:
            - Continue to the next iteration as the subset that would be formed by using nums[i] was already formed and further processed before
        - Append element at ith index to tracker.
        - Recurse with findsubs(tracker, i+1) to continue building subset tracting with current tracker
        - Pop last number to backtrack and try the next number.
    - Append a copy of tracker to subsets
- Call findsubs with empty track as tracker and index as 0
- Return subsets which contain all the possible unique subsets
'''