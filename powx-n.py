# 50. Pow(x, n)

'''
Question:
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        powr=abs(n)
        neg= True if n<0 else False
        res=1.0
        while powr>0:
            if powr%2==1:  
                res=res*x
            x=x*x
            powr//=2
        return 1/res if neg else res

'''
Explanation: 
Given: Base number float (x) and power integer (n)
Aim: To raise x to the power n without using direct pow(x,n)

Approach:
    - Set powr as the value of n disregarding its sign
    - Set neg as true if n was negative else false
    - Set res value which will contain the final result as 1.0 as x is float
    - While powr is greater than zero:
        - If powr is odd, Set res as res*x
        - Square x hence effectively halving the powr value (x^n = (x^2)^n/2)
        - Floor Divide powr by 2
    - Return 1/res if n was originally negative, else return res as it is
'''