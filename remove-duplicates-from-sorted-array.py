# 26. Remove Duplicates from Sorted Array

'''
Question:
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
- Return k.

Constraints:

1 <= nums.length <= 3 * 10^4
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        prev=1000
        for i in nums:
            if (i!=prev):
                nums[k]=i
                prev=i
                k+=1
        return k
'''
Explanation: 

Given: Array of integers sorted in non-decreasing order
Aim: To find the number of unique elements (k) and change the array such that the first k elements are all unique elements in increasing order (as we have eliminated duplicates its'll be increasing not just non-decreasing)

Approach:
- Initialize k as 0 and previous element (prev) as any element out of the range of list's element range
- Loop through the list:
    - If the current value is not the same as prev, Set element at kth index and prev as the current element and increase k by 1
- Thus we have found k and changed the first k elements to be unique and in increasing order
'''