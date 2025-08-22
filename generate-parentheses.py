# 22. Generate Parentheses

'''
Question: 
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
 
Constraints:

1 <= n <= 8
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        finlist=list()
        def dfs(finstring, opcount, size):
            if (size==(n*2)):
                finlist.append(finstring)
                return
            if opcount<n:
                dfs(finstring+'(', opcount+1, size+1)
            if opcount>(size/2):
                dfs(finstring+')', opcount, size+1)
        dfs('',0,0)
        return finlist

'''
Explanation: 
Given: integer (n) denoting number of opening brackets and closing brackets
Aim: To find all possible valid combinations using both n brackets

Approach: 
- For any combination to be valid, all brackets must be used and every closing bracket must have had an opening bracket before.
- We start with an empty string and recursively build it up while keeping track of the number of opening brackets in the string and the size of the string
- If the size string equals (2n), It would indicate all braces were used and we'll add it to our final list and end the subprocess without proceeeding further
- Then We first check whether an opening bracket can be added as we should always have an opening bracket before adding closing bracket
- If the current number of opening brackets is less than (n), We start a subprocess with string as current string appended by an open bracket with both count of '(' and size increased by 1
- Then we check if more than half the string is open brackets, implying there is atleast one open bracket unclosed. If so, We start a subprocess with string as current string appended by a close bracket with size increased by 1
- When the process ends after all its subprocesses, we would have all possible valid strings in the final list which we return
'''