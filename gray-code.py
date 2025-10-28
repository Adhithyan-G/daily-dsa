# 89. Gray Code

'''
Question:
An n-bit gray code sequence is a sequence of 2n integers where:

Every integer is in the inclusive range [0, 2n - 1],
The first integer is 0,
An integer appears no more than once in the sequence,
The binary representation of every pair of adjacent integers differs by exactly one bit, and
The binary representation of the first and last integers differs by exactly one bit.
Given an integer n, return any valid n-bit gray code sequence.
'''

class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]
        for i in range(n):
            result += [x | (1 << i) for x in result[::-1]]
        return result

'''
Explanation:
Given: An integer n
Aim: To get any valid gray code sequence that contains all integers from 0 to 2^n

Approach:
- Initialize a result list containing 0
- Loop from i = 0 until n:
    - We take every element from the reverse traversal of the result list and do bitwise OR with the binary number with all 0s but 1 at its ith index
    - We add the bitwise OR's answer to the result in the order we got it
- How the result is a gray code sequence:
    - We increase the value of i every iteration and as we start from 0, 1 << i is always a binary number that is greater that all numbers in the list before processing.
    - As the ith index will always have been 0 in the result array before the process in each iteration and all other bits of 1 << i is 0, We change only the samme one bit in all bitwise OR operations
    - The end result is gray code sequence because, We modify a bit that is of the same value (0) at the same index across all elements of the result list and that the result list is always a gray code sequence  of 2^i at every ith iteration and we append a mirror sequence of the existing sequence but with 1 at ith place
'''