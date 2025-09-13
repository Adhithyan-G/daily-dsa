# 44. Wildcard Matching

'''
Question: 
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if (len(s)!=len(p) and ('*' not in p)):
            return False
        if (not s):
            if (p.count("*")!=len(p)):
                return False
            return True
        nodupes=[]
        for i in p:
            if i=="*" and nodupes:
                if nodupes[-1]=="*":
                    continue
            nodupes.append(i)
        p=''.join(nodupes)

        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        dp[0][0] = True

        for j in range(n):
            if p[j] != '*':
                break
            dp[0][j+1] = dp[0][j]

        # Fill dp table
        for i in range(0, m):
            for j in range(0, n):
                if p[j] == s[i] or p[j] == '?':
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == '*':
                    dp[i+1][j+1] = dp[i+1][j] or dp[i][j+1]
        return dp[m][n]
        
'''
Explanation: 

Given: An input string (s) and a pattern (p)
Aim: To check whether (s) matches the pattern (p) completely

Approach: 
- Check whether the length of string and p or same, If not and there is no * in p, String cannot mathc the pattern, no Need to process, return False
- Similarly, If s is empty,
    -If everything in p is not "*", return False else return True
- Next, lets eliminate duplicate redundant "*" which are next to each other
- Initiate an empty list. For every character in p, append to list only if it is not a "*" next to a "*"
- Reset p to to string formed by joining the list
- Initiate m and n as length of s and p respectively
- Create a 2D list (dp) of dimensions n+1 and m+1 with all values as False.
- Set dp[0][0] as True indicating s and p match if they were both empty
- Set True for leading "*" which we can consider as empty if needed
- Scan through the string:
    - For every characcter in s, compare it with every character in p: 
        - If both current characters match are character in p is a "?", a Single character wildcard:
            - Set the status of the current pair as that of the last pair. That is, If everything was valid upto now, This is valid.
        - If the character is "*", Set as true If either the state of last character of s paired with current character of p (If * takes spot as some wild sequence) or current character in s and last char in p (* is considered empty) is true
- Return the fully processed state in dp[m][n]
'''