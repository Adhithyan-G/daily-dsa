# 17. Letter Combinations of a Phone Number

'''
Question:
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
'''

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        num_string_map = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']}
        final_list=['']
        for i in digits:
            curr_fin_size=len(final_list)
            for j in range(curr_fin_size):
                ap=final_list.pop(0)
                for k in num_string_map[i]:
                    final_list.append(ap+k)
        if len(final_list)==1:
            return list()
        return final_list

'''
Explanation: 

Given: A string of integers(2-9)
Known: The numbers will be mapped to alphabets as to how they are mapped in a telephone
Aim: To generate all possible strings that can be formed if each number could be representing any of their mapped strings

Approach: 
- Initiate a dictionary mapping each digit to its possible values
- Initiate final_list with an empty string
- Loop through each digit in the given string:
    - For Every digit, Loop through every element in the final_list present before starting to loop through it:
        - For every element being processed, Pop the element and loop through every possible character from the digit's mapping: 
            - Create a string by appending the character to the popped element and add it to final_list
- Now final_list contains all possible strings that could be created
- If the digits string had been empty, the final_list would contain an empty string. 
- If there is only one element in the final_list, return an empty list
- Else return final_list

What we actually did:
- We took the first digit and added every possible character as the possible strings
- If there existed next digit, We took every possible character it could be mapped to and added each to all the possible strings we determined until the last digit
- We repeated the second step until we reached the last digit and finally got all the possible strings
'''