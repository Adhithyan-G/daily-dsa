# 76. Minimum Window Substring

'''
Question:
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minsub = s+t
        charct = dict()
        for i in t:
            if i not in charct:
                charct[i] = 0
            charct[i] += 1
        allchars = len(t)
        left, right = 0, 0
        while(right < len(s)):
            currchar = s[right]
            if currchar in charct:
                charct[currchar] -= 1
                if charct[currchar] >= 0:
                    allchars -= 1
            right += 1
            while(allchars == 0):
                leftchar = s[left]
                if leftchar in charct:
                    charct[leftchar] += 1
                    if charct[leftchar] > 0:
                        allchars += 1
                        minsub = s[left:right] if (right-left) < len(minsub) else minsub
                left += 1
        return minsub if len(minsub) <= len(s) else ''

'''
Explanation:
Given: Two strings s and t.
Aim: Find the smallest substring in s that contains every character of t (including duplicates). If not possible, return "".

Approach:
- Use sliding window with two pointers left and right to dynamically track substrings in s.
- Initiate minsub as the concatenation of s and t
- Build a frequency dictionary (charct) for all characters in t.
- Maintain a counter allchars = len(t) to track how many total characters are still needed.
- Initialize left and right as 0

1. Expand window by moving right:
   - If s[right] is in charct, reduce its count.
   - If its count after reducing is still >= 0, it means we satisfied one needed character, decrement allchars.
   - Keep expanding until allchars == 0 (window now contains all chars from t).

    1.2. Shrink window by moving left while characters needed (allchars) is 0:
    - Try to minimize window size while maintaining validity.
    - When s[left] is in charct:
            - Increment its count since we're removing it.
            - If charct[s[left]] becomes > 0, it means we've just made the window invalid:
                - Increment allchars by 1
                - Record the current window s[left:right] as the smallest valid minsub if its length is smaller than length of existing minsub.
    - Move left forward to continue exploring.

- Continue the above until right reaches the end of s.

- Return minsub if it's smaller than or equal to s, else return "" (minsub being more than len(s) indicates its still s+t and hence no valid window found).
'''