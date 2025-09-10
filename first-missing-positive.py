# 41. First Missing Positive

'''
Question:
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
'''

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        size=len(nums)
        for i in range(size):
            while((nums[i] != i+1) and (0<nums[i]<=size) and (nums[nums[i]-1] != nums[i])):
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        for i in range(size):
            if nums[i] != i+1:
                return i+1
        return size+1

'''
Explanation: 

Given: An unsorted integer list (nums)
Aim: To find and return the smallest positive integer not present in nums (Like in [1,2,-4,5,2,4] the value is 3)

Approach: 
- Store the length of the list in variable (size)
- Think: If Array was sorted and consisted only of positive integers, then what would be the smallest positive integer not present? The element that is not equal to its position (index+1) as that would mean it skipped some value smaller than itself that was a positive integer!
- So Lets establish the pattern here where every position has the value as the position (Art of sorting without sorting but we don't actually sort completely)
- For each index in the array:
    - While the following conditions hold: 
        - The value (v1) is not equal to its position (index+1)
        - The value (v1) is a valid position of the list i.e, the value-1 is between or equal to range (0,size-1)
        - The value (v2) at the position indicated by value (v1) is not equal to v1, so that we won't be moving something that is already in its rightful place (which can happen if there were duplicates)
        - As long as these conditions satisfy: 
            - Swap v1 and v2, this puts v1 at its rightful place
            - Then we repeat for new v1 (former v2) until any condition breaks)
- How this is O(n)? Even though we put a while loop inside the for loop, Each swap moves an element to its rightful position and if the while made all swaps in it the very first time itself, The rest of the iterations of the for loop uses the while loop like an if condition as it'll keep failing until for loop ends. So time is O(2n) which is still O(n)

- Now sweep through our sorted but not sorted nums list and if he hit a position not containing itself as its value, return the position
- Return the size+1 if no returns were made indicating the array contained all integers in 1 to size
'''
