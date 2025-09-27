# 58. Length of Last Word

'''
Question: 
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wordcross = False
        size=0
        for i in s[::-1]:
            if i == " " and wordcross:
                return size
            if i != " ":
                wordcross = True
                size+=1
        return size

'''
Explanation: 
Given: A string (s) consisting of words and spaces
Aim: To return the length of the last word in the string

Approach:
- Initialize wordcross as False, to mark whether we have encountered a non-space character yet
- Initialize size as 0, which will store the length of the last word
- Iterate over the string in reverse (from the last character to the first):
    - If the current character is a space (" ") and wordcross is True, it means we already finished counting the last word, so return size
    - If the current character is not a space, set wordcross to True and increment size by 1
- After the loop, return size (covers the case where the last word stretches till the beginning of the string without trailing spaces)
'''