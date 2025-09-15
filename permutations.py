# 46. Permutations

'''
Question: 
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        size=len(nums)
        permus=list()
        def findpermus(perlist, pos):
            if pos==size:
                permus.append(perlist.copy())
                return
            for i in range(pos,size):
                perlist[i], perlist[pos] = perlist[pos], perlist[i]
                findpermus(perlist, pos+1)
                perlist[i], perlist[pos] = perlist[pos], perlist[i]
        findpermus(nums,0)
        return permus

'''
Explanation: 
Given: A list of unique integers (nums)
Aim: To find all possible permutations possible with the elements of the list

Approach: 
- Set size as length of the list
- Initialize an empty list (permus) to record the different permutations
- Define a helper function which we'll call recursively to find the permutations:
    - Take a list (perlist) and integer (pos) as arguements denoting rearranged list and current position to rearrange
    - If pos==size indicating a state of a complete permutation, add a copy of perlist to permus and return
    - For every index from pos to size: 
        - Swap the elements at pos index and current index in the loop in the copy
        - Recursively call the helper function with the rearranged copy and next position
        - Reverse Swap for next loop
    - Initiate recursive call with list as nums and pos as 0
    - When the function ends, We would have all permutations in the permus list which we return
'''