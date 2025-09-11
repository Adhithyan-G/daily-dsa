# 42. Trapping Rain Water

'''
Question: 
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        if(n<3):
            return 0
        left, right = 0, n-1
        lmax=rmax=water=0
        while left < right:
            if height[left] < height[right]:
                if height[left]>=lmax:
                    lmax=height[left]
                else:
                    water += lmax-height[left]
                left+=1
            else:
                if height[right]>=rmax:
                    rmax=height[right]
                else:
                    water += rmax-height[right]
                right-=1
        return water

'''
Explanation: 
Given: Array of heights between which water can be contained
Aim: To find the water that can be trapped between the heights

Approach: 
    - Set number of heights as n 
    - If n is less than 3, There would be no gap to even hold water, so return 0
    - Set left as leftmost index i.e, 0 and right as rightmost index that is n-1. We will gradually shrink the space between left and right
    - Initialize maximum value from left, right and water as 0
    - While Left is left of right:
        - If the height of left is less than that of right:
            - then right height is more important and we have to left toward right
            - If value of left index is greater than the maximum value observed from left(lmax), Set lmax as value at left index as this would be the greatest height observed from left
            - Else, Add the difference between the lmax and height to water
            - Move left to left+1
        - Else: 
            - Do the same checking and water updation for right and rmax and then move right to right-1
    - Return water which would now indicate the volume of water being stored
'''
