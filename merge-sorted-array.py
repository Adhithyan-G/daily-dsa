# 88. Merge Sorted Array

'''
Question:
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1 = m-1
        n2 = n-1
        for pos in range(-1, -(m+n+1), -1):
            if n1 == -1:
                nums1[pos] = nums2[n2]
                n2-=1
            elif n2 == -1:
                nums1[pos] = nums1[n1]
                n1-=1
            elif nums1[n1] >= nums2[n2]:
                nums1[pos] = nums1[n1]
                n1-=1
            else:
                nums1[pos] = nums2[n2]
                n2-=1

'''
Explanation:
Given: Two sorted integer arrays nums1 (size m + n) and nums2 (size n)
Aim: Merge nums2 into nums1 in non-decreasing order without using extra space

Approach:
- Since nums1 has enough trailing zeros to hold all elements, we merge from the end to avoid overwriting.
- Initialize pointers:
    - n1 = m - 1 -> index of last element in nums1 (Greatest in nums1)
    - n2 = n - 1 -> index of last element in nums2 (Greatest in nums2)
    - pos = index of the last position in nums1 (start from -1 for reverse traversal)
- For each position (pos) from the end to the start:
    - If nums1 has no remaining valid elements (n1 == -1), copy remaining nums2 elements
    - If nums2 is exhausted (n2 == -1), nums1 is already complete
    - Otherwise, compare nums1[n1] and nums2[n2]:
        - If nums1[n1] >= nums2[n2], place nums1[n1] at nums1[pos]
        - Else, place nums2[n2] at nums1[pos]
    - Decrement the used pointer (n1 or n2) accordingly
'''