# 55. Jump Game

'''
Question:
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        if size==1:
            return True
        left = 0
        jumpstart = 0
        while (True):
            maxval = -999999
            print(left)
            jump=nums[left]
            if (left+jump)>=(size-1):
                return True
            if (left+jump)<=jumpstart:
                return False
            orgleft = left
            for i in range(jumpstart, orgleft+jump+1):
                val = (nums[i] - jump) + (i-orgleft)
                if (val > maxval):
                    maxval = val
                    left = i
            jumpstart=orgleft+jump

'''
Explanation: 
Given: A list of integers (nums)
Aim: To determine whether the last element can be reached by jumping maximum the value of index we jump from

Approach:
- Set size as length of the list
- If size is 1, Then we are already at the last position, return True
- Initialize left and jumpstart as 0
- Loop:
    - Initialize maxval as -999999 (Any unreachable negative number will do)
    - Get the distance jumpable from current left index and store it as jump
    - If maximum distance that can be covered by jump from left reaches or crosses the last index, return True
    - If maximum distance that can be covered by jump from left does not even cross jumpstart of this iteration, We are stuck in the current position, Return False.
    - Set orgleft as left (To track the original left index as we would modify the left index)
    - For every element from jumpstart index to maximum jump from left index (Including the maximum jump):
        - Calculate val to be the difference in jumping potential between current element and left element and sum the positional difference between the current and the original left indices to calculate actual maximum coverage
        - If val is greater than maxval:
            - Set maxval as val, Set left as index of current element of the iteration
    - Start considering next jumpstart position from the jump index from the original left before the processing of elements in the range
'''