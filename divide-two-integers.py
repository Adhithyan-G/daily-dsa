# 29. Divide Two Integers

'''
Question:

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, and if the quotient is strictly less than -2^31, then return -2^31.
'''

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend==(-2147483648) and divisor==(-1)):
            return 2147483647
        if ((dividend<0 and divisor<0) or (dividend>0 and divisor>0)):
            qpos=True
        else:
            qpos=False
        dividend=abs(dividend)
        divisor=abs(divisor)
        quotient=0
        add2=1
        while(dividend>=divisor):
            divisor=divisor+divisor
            add2=add2<<1
        add2=add2>>1
        divisor=divisor>>1
        while(divisor>0 and dividend>0):
            if (dividend>=divisor):
                dividend=dividend-divisor
                quotient=quotient+add2
            add2=add2>>1
            divisor=divisor>>1
        return quotient if qpos else -quotient

'''
Explanation: 
Given: Two integers, dividend and divisor
Aim: To divide dividend by divisor without using multiplication, division, and mod operator 
(The art of dividing without dividing)

Approach: 
- The only case when the value exceeds 2^31-1 is when we have -(2^31) and -1. So we return 2^31-1 in that case
- Then we decide whether the quotient will be negative or not by comparing whether both given integers are of same sign or not. qpos is set true if they are of same sign else it is set as false
- We set both integers to their bsolute value as we know the quotient sign
- While the dividend is larger or equal to divisor, we double the divisor and keep track how much times of the original divisor it is. (Art of doubling without doubling but adding to itself and left shift of bits)
- Once divisor exceeds dividend, we half it and the tracker(add2) (Right shift of bits)
- Now until both dividend and divisor are above 0:
    - If dividend is greater than or equal to divisor, We subtract divisor from dividend and add the tracker value to quotient
    - We half the dividend and the tracker(add2) (Right shift of bits)
-  Now we have the quotient which we return if it is supposed to be positive or its negative if its supposed to negativve by using qpos
'''