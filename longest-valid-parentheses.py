# 32. Longest Valid Parentheses

'''
Question:
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        opct=0
        enct=0
        maxlen=0
        templen=0
        for i in range(0,len(s)):
            if s[i]=='(':
                opct+=1
            if s[i]==')':
                enct+=1
            if(enct==opct and (maxlen<(2*enct))):
                maxlen=2*enct
            if(enct>opct):
                opct, enct = 0, 0
        opct, enct = 0, 0
        for i in s[::-1]:
            if i==')':
                enct+=1
            if i=='(':
                opct+=1
            if(enct==opct and (maxlen<(2*enct))):
                maxlen=2*enct
            if(opct>enct):
                opct, enct = 0, 0
        return maxlen

'''
Explanation: 
Given: A string consisting of '(' and ')'
Aim: To find the length of the longest valid parantheses

Approach:
- Initiate opct(count of opening braces), enct(count of ending braces), maxlen(Maximum length of valid substring) as 0
- For every character in string (s):
    - If it is a opening brace, increase opct by 1
    - If it is a closing brace, increase enct by 1
    - If enct and opct are equal we have a complete valid parantheses substring. Set maxlen to double of enct if it is smaller than double of enct
    - If enct is greater than opct, We have an end brace with nothing to close! Reset everything except maxlen to 0
- Now we have handled case for when we might have unmatching ')', We need to repeat the same for the reverse of string checking for unmatched '('.
- Return maxlen after checking both ways
'''