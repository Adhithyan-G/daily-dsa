# 47. Permutations II

'''
Question: 
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size=len(nums)
        permus=list()
        def findpermus(perlist, pos):
            if pos==size:
                permus.append(perlist.copy())
                return
            for i in range(pos,size):
                if i>pos and nums[i]==nums[i-1]:
                    continue
                perlist[i], perlist[pos] = perlist[pos], perlist[i]
                findpermus(perlist, pos+1)
                perlist[i], perlist[pos] = perlist[pos], perlist[i]
        findpermus(nums,0)
        return permus

'''
Explanation: 
Given: A list of integers with duplicates possible (nums)
Aim: To find all possible unique permutations possible with the elements of the list

Approach: 
- Sort the List to have duplicates together.
- Set size as length of the list
- Initialize an empty list (permus) to record the different permutations
- Define a helper function which we'll call recursively to find the permutations:
    - Take a list (perlist) and integer (pos) as arguments denoting rearranged list and current position to rearrange
    - If pos==size indicating a state of a complete permutation, add a copy of perlist to permus and return
    - For every index from pos to size: 
        - If the index is greater than pos and element at last index was the same as this index, skip to next iteration as we already have the value fixed upto pos for this value
        - Swap the elements at pos index and current index in the loop
        - Recursively call the helper function with the rearranged list and next position
        - Reverse Swap for next loop
    - Initiate recursive call with list as nums and pos as 0
    - When the function ends, We would have all permutations in the permus list which we return
'''