# Combination Sum II

'''
Question: 
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=list()        
        def combMake(start, combi, total):
            if total == target:
                res.append(combi.copy())
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                if i != start and candidates[i]==candidates[i-1]:
                    continue
                combi.append(candidates[i])
                combMake(i+1, combi, total + candidates[i])  
                combi.pop()

        combMake(0, [], 0)
        return res

'''
Explanation:
Given: A list of integers (candidates) and an integer (target)
Aim: To find all possible unique combinations possible from the candidates to form target via summing them where each element can only be used once ([1,2] 1 can be used only onse, [1,2,1] here 1 can be used only twice)

Approach:
- Initiate an empty list as res which will have the final resulting list
- Sort the candidates list so that we can easily avoid duplicates while processing as duplicates would be next to each other if sorted
- Make a function using which we construct the combinations recursively:
    - The function combMake takes start index, the combination upto now and the total of the combination upto now as arguments
    - If the total is equal to target, add a copy of the combination to res and return (We add a copy because lists are passed by reference and as we pop and append elements to the combination list in the function, We'll end up modifying the lists in res too if we add the combi instead of its copy)
    - If total is greater than target, return as we have crossed target
    - Loop from the start index to length of the candidates list:
        - If the index is not the start index and the element is the same as the previous element, skip over to the next iteration in order to avoid duplicate combinations where in the given position, same value but different elements would be present.
        - Append the element to combi
        - Recursively call the function with the next index as start, updated combination list and updated total (We use next index as repetitions of the same element are not allowed)
        - When the recursion branch ends and gets back here, pop the appended element to refresh the combination list
- Start combMake with 0 as start, an empty list and 0 as total
- Return res
'''
