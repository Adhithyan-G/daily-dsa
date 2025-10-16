# 77. Combinations

'''
Question:
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.
'''

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = list()
        comb = list()
        def recbuild(index, needed):
            if needed == 0:
                res.append(comb.copy())
                return
            for i in range(index, n+1):
                comb.append(i)
                recbuild(i+1, needed-1)
                comb.pop()
            return
        recbuild(1, k)
        return res

'''
Explanation:
Given: Two integers n and k.
Aim: To return all possible combinations of k numbers chosen from the range [1, n].

Approach:
- Use Backtracking:
    - Maintain:
        - comb -> current combination being built
        - res -> list to store all complete combinations
    - Define a recursive function recbuild(index, needed):
        - If needed == 0:
            - No more elements needed hence current combination is complete, so add a copy of comb to res and then return
        - Else:
            - For i from index to n:
                - Append i to comb.
                - Recurse with recbuild(i+1, needed-1) to fill the remaining slots.
                - Pop i to backtrack and try the next number.
- Start recursion with recbuild(1, k).
- Return res list containing all unique combinations of length k from numbers 1 through n.
'''