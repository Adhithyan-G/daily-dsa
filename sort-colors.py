# 75. Sort Colors

'''
Question:
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        left = 0
        right = n-1
        index = 0
        while(index <= right):
            if nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                index+=1
                left+=1
            elif nums[index] == 2:
                nums[right], nums[index] = nums[index], nums[right]
                right-=1
            else:
                index+=1
        
'''
Explanation:
Given: An integer array nums containing 0 (red), 1 (white), and 2 (blue).
Aim: To sort the array in-place in the order red -> white -> blue.

Approach:
- We need to group all 0s to the left and all 2s the right and this will naturally place all 1s in the center
- Use three pointers:
    - left -> next position to place 0
    - right -> next position to place 2
    - index -> current scanning position
- Traverse the array while index is not greater than right:
    - If nums[index] == 0:
        - Swap nums[index] with nums[left].
        - Move both left and index forward.
    - If nums[index] == 2:
        - Swap nums[index] with nums[right].
        - Move right backward, We don't move index here as the old right's value could be 0 or 2. We can move index for value being zero because we know value at left can only be 1 as left is always less than or equal to index and left would have already been checked whether it was 0 or 2
    - Else:
        - Just Move index forward as 1s will automatically get placed in the remaining center after we push all 0s to the left and 2s to the right
- The List will now be sorted
'''