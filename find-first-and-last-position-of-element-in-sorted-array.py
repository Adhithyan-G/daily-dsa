# 34. Find First and Last Position of Element in Sorted Array

'''
Question: 
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
'''
def binsearch(l, start, end, target, typ):
    ind=-1
    while(start<=end):
        mid=(start+end)//2
        if (target==l[mid]):
            ind=mid
            if typ=='l':
                end=mid-1
            else: 
                start=mid+1
        elif (target<l[mid]):
            end=mid-1
        else:
            start=mid+1
    return ind

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        size=len(nums)
        l=binsearch(nums,0,size-1,target,'l')
        r=binsearch(nums,0,size-1,target,'r')
        return [l,r]
        
'''
Explanation:
Given: An array (nums) sorted in non-decreasing order and an integer (target)
Aim: To find the starting and ending inclusive indices of the target if exists

Approach: 
- We do our classic binary search with a little twist...
- Define a function for binary search taking the list, start index, end index, target value and type (typ) of search (what is this type of search???)
    - We initialize ind as -1 which will finally depict the index of the target value
    - While start is not greater than end:
        - Floor divide the sum of start and end by 2 and set as mid
        - If value at mid is equal to target: 
            - Set ind as mid (We found target! We're done right? RIGHT?..... Nah)
            - If typ is 'l', set end as mid-1 else set start as mid+1 (Hence having us search for the leftmost target index or the rightmost target index using the typ value instead of breaking the search as soon as we hit target)
        - If value is greater than target - Set end to mid-1
        - Else, set start to mid+1
    - Have the function return ind
- Binary search with our function with typ as 'l' to find leftmost index of target
- Binary search with our function with typ as 'r' to find rightmost index of target
- Return [l,r]
'''

