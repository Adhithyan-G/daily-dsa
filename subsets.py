# 78. Subsets
'''
Question:
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = list()
        comb = list()
        def recbuild(index, needed):
            if needed == 0:
                res.append(comb.copy())
                return
            for i in range(index, len(nums)-needed+1):
                comb.append(nums[i])
                recbuild(i+1, needed-1)
                comb.pop()
            return
        for i in range(0, len(nums)+1):
            recbuild(0, i)
        return res

'''
Explanation:
Given: An integer array nums of unique elements.
Aim: To return all possible subsets (the power set) without duplicates.

Approach:
- Every subset can be seen as a combination of size k, where k ranges from 0 to n.
- Maintain:
        - comb -> current combination being built
        - res -> list to store all complete combinations
- Define a recursive function recbuild(index, needed):
    - If needed == 0:
        - No more elements needed hence current combination is complete, so add a copy of comb to res and then return
    - Else:
        - For i from index to len(nums)-needed+1: ((len(nums)-needed+1) Helps us prune trees which will ultimately fail i.e, never reach needed == 0)
            - Append element at ith index to comb.
            - Recurse with recbuild(i+1, needed-1) to fill the remaining slots.
            - Pop last number to backtrack and try the next number.
- Call recursive combination build for every number of elements from 0 to n
- Return res which would contain all the possible subsets
'''