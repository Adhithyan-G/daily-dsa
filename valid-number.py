# 65. Valid Number

'''
Question:
Given a string s, return whether s is a valid number.

For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".

Formally, a valid number is defined using one of the following definitions:

An integer number followed by an optional exponent.
A decimal number followed by an optional exponent.
An integer number is defined with an optional sign '-' or '+' followed by digits.

A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:

Digits followed by a dot '.'.
Digits followed by a dot '.' followed by digits.
A dot '.' followed by digits.
An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.

The digits are defined as one or more digits.

'''
class Solution:
    def isNumber(self, s: str) -> bool:
        gotNum = False
        expectNum = True
        inExpon = False
        inDeci = False
        last = ""
        n = len(s)
        for i in range(n):
            c = s[i]
            if c not in ['+', '-', '.', 'E', 'e'] and (ord(c) < 48 or ord(c) > 57):
                return False
            if c in ['+', '-']:
                if i != 0 and last not in ['e', 'E']:
                    return False
            if c == '.':
                if inExpon or inDeci:
                    return False
                if not gotNum:
                    expectNum = True
                inDeci = True
            if ord(c) >= 48 and ord(c) <= 57:
                gotNum = True
                expectNum = False
            if c in ['E', 'e']:
                if not gotNum or inExpon:
                    return False
                inExpon = True
                expectNum = True
            last = c
        if expectNum:
            return False
        return True

'''
Explanation:  
Given: A string s  
Aim: To check whether s is a valid number as per integer/decimal/exponent rules  

Approach:  
- Maintain flags to track parsing state:  
    - gotNum → whether we have seen at least one digit  
    - expectNum → whether we are expecting a digit next (e.g. after exponent)  
    - inExpon → whether we are currently inside exponent part  
    - inDeci → whether we already used a decimal point  
- Traverse each character c of the string:  
    - If c is not a digit or one of (+, -, ., e, E): return False immediately  
    - If c is '+' or '-': valid only at beginning or right after exponent, else return False
    - If c is '.':
        - Invalid if already inside exponent or if decimal already used  
        - If no digits yet, still allow but keep expecting digit  
        - Mark decimal as used  
    - If c is a digit:
        - Mark gotNum = True and we no longer expect a digit
    - If c is 'e' or 'E':
        - Valid only if digits have already appeared and no exponent seen yet
        - Mark that we are now inside exponent and must see digits next → expectNum = True
- After traversal:
    - If still expectNum (e.g. string ended when we were expecting a digit) → return False
    - Else return True
'''