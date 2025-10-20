# 81. Search in Rotated Sorted Array II

'''
Question:
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.
'''

class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True

            while left < right and nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

'''
Explanation:
Given: A sorted list of integers in non-decreasing order that is left rotated with an unknown pivot index
Aim: To find target element as optimal as possible

Approach:
- Initialize left as 0 and right as size of list minus 1
- While left<=right:
    - Set mid as floor division of sum of left and right, by 2
    - If the mid element is the target, return True
    - Handle duplicates by moving left and right pointers toward each other if they are duplicates of mid
    - If the left element is less than or equal to mid element:
        - It means the left of mid is sorted in ascending order left to mid.
        - If target is greater than or equal to left and also less than mid element, We move right to mid -1 as it means target is in this range else, move left to mid+1 as the target isn't in the sorted range
    - Else, It implies the right side is sorted.
        - If the target is less than or equal to right element and greater than mid element, It means its in the right range, set left to mid+1
        - Else its not in the right range, set right to mid-1
- If we reach outside the loop without returning, It means the target does not exist.
- Return false to indicate target not present
'''