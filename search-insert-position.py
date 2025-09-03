# 35. Search Insert Position

'''
Question: 
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''

def binsearch(nums, target):
    left=0
    right=len(nums)-1
    while (left<=right):
        mid=(left+right)//2
        if (nums[mid]==target):
            return mid
        elif (nums[mid]>target):
            right=mid-1
        else:
            left=mid+1
    return left
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return binsearch(nums,target)

'''
Explanation: 
Given: An array (nums) sorted in non-decreasing order and an integer (target)
Aim: To find index of target if exists else return index to insert it

Approach:
- Do binary search with initializing left as 0 and right as size-1
- If target is found, return mid
- Return left, which will be triggered only if target was not found and would indicate position to insert element
'''