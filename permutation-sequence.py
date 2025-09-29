# 60. Permutation Sequence

'''
Question:
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
'''
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        totalpermu = 1
        nums = list()
        for i in range(1,n+1):
            totalpermu*=i
            nums.append(i)
        totalpermu = totalpermu
        k-=1
        respermu = ""
        for i in range(n, 0, -1):
            if k==0:
                for i in nums:
                    respermu=respermu+str(i)
                break
            totalpermu/=i
            pos = int(k//totalpermu)
            respermu = respermu+(str(nums.pop(pos)))
            k = k%totalpermu
        return respermu

'''
Explanation:
Given: Two integers n and k
Aim: To find the k-th permutation sequence of the set [1, 2, ..., n] in lexicographic order


Approach:
- Initialize totalpermu as 1 and an empty list nums
- For every integer from 1 to n:
    - Multiply totalpermu with current integer
    - Append the integer into nums
- Decrease k by 1 (Index is from 0 to n!-1 not 1 to n!)
- Initialize empty string respermu
- Loop from n down to 1:
    - If k is 0, No need to process more, just append every number left in nums in the same order and break the loop
    - Divide totalpermu by current index (this represents the number of permutations per number at this position)
    - Get index pos = k // totalpermu
    - Append the number at nums[pos] to respermu
    - Remove the used number from nums
    - Update k as remainder when divided by totalpermu
- After loop ends, return respermu
'''