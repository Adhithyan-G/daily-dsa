# 33. Search in Rotated Sorted Array

'''
Question: 
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while(left<=right):
            mid = (left+right)//2
            ele=nums[mid]
            if (ele==target):
                return mid
            if (nums[left]<=ele):
                if nums[left]<=target and target<ele:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if nums[right]>=target and target>ele:
                    left=mid+1
                else:
                    right=mid-1
        return -1

'''
Explanation:
Given: A sorted list of integers in ascending order that is possibly left rotated at an unknown index
Aim: To find target element in O(logn)

Approach:
- Initialize left as 0 and right as size of list minus 1
- While left<=right:
    - Set mid as floor division of sum of left and right, by 2
    - If the mid element is the target, return mid
    - If the left element is less than or equal to mid element:
        - It means the left of mid is sorted in ascending order left to mid.
        - If target is greater than or equal to left and also less than mid element, We move right to mid -1 as it means target is in this range else, move left to mid+1 as the target isn't in the sorted range
    - Else, It implies the right side is sorted.
        - If the target is less than or equal to right element and greater than mid element, It means its in the right range, set left to mid+1
        - Else its not in the right range, set right to mid-1
- If we reach outside the loop without returning, It means the target does not exist. Return -1 to indicate it
'''
