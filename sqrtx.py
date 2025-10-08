# 69. Sqrt(x)

'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        if (x == 0 or x == 1):
            return x
        top = x
        mini = 1
        while((top-mini)>1):
            mid = (top+mini)//2
            if ((mid*mid) == x):
                return mid
            if (mid*mid) < x:
                mini = mid
            else:
                top = mid
        return mini

'''
Explanation:
Given: A non-negative integer x.
Aim: To compute and return the integer part (floor) of the square root of x without using built-in exponentiation functions.

Approach:
- Handle base cases:
  - If x is 0 or 1, return x directly since root of 0 = 0 and root of 1 = 1.
- Use binary search to find the largest integer whose square is closest to x.
  - Initialize:
    - mini = 1  (lower boundary of the search range.)
    - top = x  (upper boundary of the search range.)
- Repeat while the search range is larger than 1 (i.e., (top - mini) > 1):
  - Compute mid = (top + mini) // 2 (integer midpoint).
  - If mid^2 equals x, return mid (perfect square case).
  - If mid^2 < x, move the lower boundary up (mini = mid) to search higher.
  - Else, move the upper boundary down (top = mid) to search lower.
- When the loop ends, mini will hold the integer part of root of x.
- Return mini as the floored square root value.
'''