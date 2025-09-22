# 53. Maximum Subarray
'''
Question: 
Given an integer array nums, find the subarray with the largest sum, and return its sum.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = nums[0]
        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        return max_sum

'''
Explanation: 
Given: A list of integers
Aim: To find and return the sum of the subarray with the largest sum

Approach:
- Initialize max_sum and curr_sum as the first element where max_sum would always indicate the maximum sum at any point and curr_sum would represent the updated sum while traversing through the array
- Traverse through the rest of the array: 
    - Assign the maximum of the sum of the current element and curr_sum (Extending the subarray) or the current element (Reset and start new subarray would be better). This helps us handle negative elements
    - If curr_sum is greater than max_sum, set max_sum as curr_sum
- Return max_sum denoting the largest sum
'''