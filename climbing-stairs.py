# 70. Climbing Stairs

'''
Question:
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 2
        for i in range(2,n):
            a, b = b, a+b
        return n if n == 1 else b

'''
Explanation:
Given: An integer n representing the total number of steps to reach the top.
Aim: To find the number of distinct ways to climb to the top when each move can be either 1 step or 2 steps.

Approach:
- To reach step n, one must have arrived from either:
    - Step (n−1) by taking a single step, or
    - Step (n−2) by taking a double step.
- Hence, total ways to reach step n = ways(n−1) + ways(n−2).
- Initialize:
    - a = 1  (ways to reach step 1)
    - b = 2  (ways to reach step 2)
- For each step from 2 to n:
    - Set number of ways to reach this step as sum of last and two steps before as we can climb either 1 or 2 steps at a time
    - Set number of ways to reach the before step as original b
- Return n if there's only one step else b which denotes the total ways to reach step n.
'''