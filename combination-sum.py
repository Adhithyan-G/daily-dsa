# 39. Combination Sum

'''
Question:
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
'''

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res=list()        
        def combMake(start, combi, total):
            if total == target:
                res.append(combi.copy())
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                combi.append(candidates[i])
                combMake(i, combi, total + candidates[i])  
                combi.pop()

        combMake(0, [], 0)
        return res

'''
Explanation:
Given: A list of distinct integers (candidates) and an integer (target)
Aim: To find all possible unique combinations possible from the candidates to form target via summing them where elements can be repeated as many times as wanted

Approach:
- Initiate an empty list as res which will have the final resulting list
- Make a function using which we construct the combinations recursively:
    - The function combMake takes start index, the combination upto now and the total of the combination upto now as arguments
    - If the total is equal to target, add a copy of the combination to res and return (We add a copy because lists are passed by reference and as we pop and append elements to the combination list in the function, We'll end up modifying the lists in res too if we add the combi instead of its copy)
    - If total is greater than target, return as we have crossed target
    - Loop from the start index to length of the candidates list:
        - Append the element to combi
        - Recursively call the function with current index as start, updated combination list and updated total ( We use current index as repetitions of the same element are allowed but not 0 index as we need unique combinations)
        - When the recursion branch ends and gets back here, pop the appended element to refresh the combination list
- Start combMake with 0 as start, an empty list and 0 as total
- Return res
'''
