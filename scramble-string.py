# 87. Scramble String

'''
Question:
We can scramble a string s to get a string t using the following algorithm:

If the length of the string is 1, stop.
If the length of the string is > 1, do the following:
Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
Apply step 1 recursively on each of the two substrings x and y.
Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.
'''

from collections import Counter

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        track = {}
        def compareParts(a, b):
            if (a, b) in track:
                return track[(a, b)]
            if a == b:
                return True
            if Counter(a) != Counter    (b):
                return False
            n = len(a)
            for i in range(1, n):
                # Break but don't swap
                if compareParts(a[:i], b[:i]) and compareParts(a[i:], b[i:]):
                    track[(a, b)] = True
                    return True
                # Break and Swap
                if compareParts(a[:i], b[-i:]) and compareParts(a[i:], b[:-i]):
                    track[(a, b)] = True
                    return True
            track[(a, b)] = False
            return False
        return compareParts(s1, s2)

'''
Explanation: 
Given: Two Strings s1 annd s2
Aim: To check whether s2 is a scrambled version of s1

Approach:
- Scrambling can be done by splitting up anywhere in the string as long as the parts are non empty and the parts can either be swapped or kept as is and then the parts can also be further scrambled recursively

- We'll create an empty dictionary (track) to track two parts are the scrambled version of each other or not
- Define a function compareParts that takes in two strings (a) and (b):
    - If this pair of (a,b) have been compared before, fetch and return its comparison result from track
    - If a and b are the same, return True
    - If a abd b don't have the same characters and number of those characters, No scrambling can make them match, return False
    - Set n as length of a (or b, they are of equal length)
    - For every index from 1 to n: (Can't take 0 as 0 would cause a empty substring)
        - First we compare slicing without swapping the parts.
        - We slice both the strings at i and compare both the pairs of parts. If they are valid, We set track[(a,b)] as True and return True
        - Now that we have tried slicing without swapping and it wasn't valid, Try for slice and swap next
        - With slicing of a at i, 
           (i) The first part of a should be compared with the second part of b sliced at i from the end 
           (ii) And the vice Versa must also be valid
           - If both conditions satisfy, Set track[(a,b)] as True and return True
    - Set track[(a,b)] as False and Return False as Both the No-Swap and Swap scrambling comparisons failed
- Start compareParts with (s1, s2) and return the final result
'''