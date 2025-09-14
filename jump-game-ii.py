# 45. Jump Game II

'''
Question: 
You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        size=len(nums)
        if size==1: 
            return 0
        if(nums[0]>=size-1):
            return 1
        lind=0
        jumps=0
        coverleft=99999
        stval=lind+1
        while(True):
            maxjump=nums[lind]
            endind=lind+maxjump+1
            if (endind>=size):
                return jumps+1
            for i in range(stval, min(size,endind)):
                dist=size-i-1
                afterjump=dist-nums[i]
                if afterjump<coverleft:
                    coverleft=afterjump
                    lind=i
            stval=endind
            jumps+=1
            
'''
Explanation: 

Given: A list of non-negative integers with each element denoting the maximum possible jump distance
Aim: To Find the minimum number of jumps needed to reach the last index

Approach: 
- Set size as length of the list
- If its a single element, return 0
- If the initial element itself can jump directly to last element, return 1 
- We don't check for Initial element being zero or for cases where we'll bestuck at a zero spot as we are guaranteed to get only cases where we reach last index
- Set left index as 0, jumps as 0 and coverleft as 99999 (Any number bigger than the list size itself)
- Set stval as lind+1 (The index from we which we should consider positions)
- Loop: 
    - Get maxminum jumpable distance from nums[lind] and set it as maxjump
    - Set endind as maxjump from lind+1
    - If endind is greater than equal size, return jumps+1 as we reach last index in a jump
    - For every index in range from stval to index (endind or size if size is lesser):
        - Calculate the distance between last position and current position as dist
        - Calculate where we'll be if we jump the maximum distance from this position as afterjump
        - If afterjump is less than coverleft:
            - Set coverleft as afterjump
            - Set lind as i
    - Update stval to stval+maxjump+1 to leave out already processed and deemed unoptimal tiles for the next iteration saving processing time (This lets us do this Time complexity of O(n))
    - Incremant Jumps by 1
'''
