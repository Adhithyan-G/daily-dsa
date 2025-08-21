# 20. Valid Parentheses

'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = [0]
        for i in s: 
            if i=='(' or i=='{' or i=='[':
                stack.append(i)
            else:
                cmpele=stack.pop()
                if cmpele==0:
                    return False
                elif i==')' and cmpele=='(':
                    continue
                elif i==']' and cmpele=='[':
                    continue
                elif i=='}' and cmpele=='{':
                    continue
                else:
                    return False
        if(stack.pop()==0):
            return True
        return False

'''
Explanation: 
Given: a string consisting only of brackets
Aim: To validate whether the given string fulfils given condition

Approach: 
- Initialize an stack with 0 denoting stack end to add open brackets
- Loop through the string:
    - If it is a open bracket, append the bracket to the stack
    - If not, 
        - If the stack is empty, Then we have a close bracket without any open bracket, hence string is invalid -> return false
        - Pop the last element and check if current close bracket matches the popped open bracket
            - If they don't match return false as they don't correspond else continue traversing through the string
- After the string has been completely traversed, Check if stack is empty
- If empty, all brackets were closed in correct order, return true
- Else some brackets are still left open, So return false.

Time Complexity: O(n) where n is the length of string
'''