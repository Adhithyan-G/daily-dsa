# 66. Plus One

'''
Question:
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 0
        for i in range(-1, -(n+1), -1):
            digisum = digits[i]+1
            if digisum == 10:
                digits[i] = 0
                carry = 1
            else:
                digits[i] = digisum
                carry = 0
            if carry == 0:
                break
        if carry == 1:
            return [1]+digits
        return digits

'''
Explanation:
Given: A list digits representing a non-negative integer with no leading zeros.
Aim: To increment the integer by one and return the resulting list of digits.

Approach:
- Initialize variable n as the length of digits and carry as 0.
- Traverse the digits from rightmost to leftmost using negative indexing:
    - Add 1 to the current digit.
    - If the result equals 10:
        - Set the current digit to 0 and carry over 1 to the next digit on the left.
    - Else:
        - Update the current digit with the new value and stop further iteration as no carry remains.
- After completing traversal, if carry still equals 1 (as in the case of all digits being 9), prepend 1 to the digits list to handle overflow.
- Return the final digits list representing the incremented integer.
'''