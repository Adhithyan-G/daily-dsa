# 67. Add Binary

'''
Question:
Given two binary strings a and b, return their sum as a binary string.
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(('0b'+a),2)+int(('0b'+b),2))[2:]

'''
Explanation:
Given: Two binary strings a and b representing binary numbers.
Aim: To return their sum as a binary string.

Approach:
- Prefix both input strings with '0b' to make them valid Python binary literals.
- Convert each to an integer using int(<string>, 2) which interprets them as base-2 numbers.
- Add the two integer values directly.
- Convert the result back to a binary string using bin(<sum>), which returns a string prefixed with '0b'.
- Slice the string from index 2 onwards ([2:]) to remove the '0b' prefix and obtain the pure binary digits.
- Return the resulting binary string as the sum.
'''