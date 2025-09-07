# 38. Count and Say

'''
Question: 
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).
Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say sequence.

'''

class Solution:
    def countAndSay(self, n: int) -> str:
        res="1"
        for i in range(1,n):
            val=res[0]
            ct=0
            newres=""
            for j in res:
                if val==j:
                    ct+=1
                else:
                    newres=newres+str(ct)+val
                    ct=1
                    val=j
            newres=newres+str(ct)+val
            res=newres
        return res

'''
Explanation:
Given: An integer (n)
Aim: To find the nth element of the count-and-say sequence

Approach:
- Initate res which will be the result string as "1"
- Loop until we reach n:
    - Set val as the first character and track count of character with ct initialized as 0 and the result we'll have after this iteration as newres
    - For every character (j) in the res string:
        - If j is the same as val (the character before j), increaase ct by 1
        - Else, append ct as string followed by val to newres and set val to j and reset ct to 1
    - Append ct as string followed by val to newres as the last unique character(s) would not have been recorded
    - Set res and newres and repeat for next iteration
- Return res which will contain the required string
'''