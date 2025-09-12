# 43. Multiply Strings

'''
Question: 
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if (num1=='0' or num2=='0'):
            return '0'
        mul2=-1
        res=[0 for i in range(len(num1)+len(num2))]
        for i in num2[::-1]:
            n2=(ord(i)-ord('0'))
            mul1=0
            for j in num1[::-1]:
                n1=(ord(j)-ord('0'))
                prod=n2*n1
                place=mul1+mul2
                carry=0
                while(prod>=1):
                    temp = (res[place]+prod%10)
                    res[place], carry = (temp+carry)%10, (temp+carry)//10
                    place-=1
                    prod=prod//10
                while(carry!=0):
                    temp = res[place]+carry
                    res[place],carry = temp%10, temp//10
                    place-=1
                mul1=mul1-1
            mul2=mul2-1
        ind=0
        if res[0]==0:
            ind=1
        res = [str(i) for i in res[ind:]]
        return "".join(res)

'''
Explanation:

Given: Two non-negative integers as strings (num1, num2)
Aim: To multiply them without converting the inputs to integer directly

Approach: 
- As We can't convert the inputs to integers directly, Lets break them into single digits and do the old-school math
- If either are zero, return zero
- Initialize multiplier of the current digit of the second number as -1 (mul2)
- Initialize list res of the combined size of the strings populated with 0s 
- Process through the num2 in reverse (ones to tens to hundreds and so on):
    - Set n2 as the difference between the ASCII values of the digit of num2 as character and '0'
    - Set multiplier of the current digit of the first number as 0 (mul1)
    - Process through the num1 in reverse (ones to tens to hundreds and so on):
        - Set n1 as the difference between the ASCII values of the digit of num1 as character and '0'
        - Multiply n1 and n2 and set it as prod
        - Determine the place of the digit(1th, 10th, 100th etc) where this product is supposed to be added by adding mul1 and mul2
        - Initialize carry as 0
        - While prod is greater than or equal to 1:
            - Take the value already at current place in res and add it to the digit at lowest value place of prod and set it as temp
            - Set the digit in specified place in res as the lowest value place of temp
            - Floor divide temp by 10 to get the carry value
            - Decrease place by 1
            - Floor divide prod by 10 to move to the next digit in prod
        - While carry exists, Keep adding carry to higher places until there is no carry
        - Decrease mul1 by 1
    - Decrease mul2 by 1
- Only the first digit can be zero for preceeding zeros with given constraints as the smallest n-digit number and m-digit numbers are powers of 10
- Convert the numbers in res to characters without the preceeding zero if exists
- Return res which would contain the final product as string
'''