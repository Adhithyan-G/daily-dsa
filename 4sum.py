# 18. 4Sum

'''
Question: 
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]


Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''

class Solution:
    def fourSum(self, nums: list[int], target: int) -> List[List[int]]:
        siz=len(nums)
        if (siz<4):
            return list()
        nums.sort()
        finlist=list()
        for i in range(0,siz-3):
            fix_val_a=nums[i]
            for j in range(i+1,siz-2):
                fix_val_b=nums[j]
                tempsum=fix_val_a+fix_val_b
                left=j+1
                right=siz-1
                while(left<right):
                    finsum=tempsum+nums[left]+nums[right]
                    if finsum==target:
                        finlist.append(tuple([fix_val_a,fix_val_b,nums[left],nums[right]]))
                        left+=1
                        right-=1
                    elif finsum<target:
                        left+=1
                    elif finsum>target:
                        right-=1
        finlist=set(finlist)
        finlist=[i for i in finlist]
        return finlist

'''
Explanation: 

Given: An array of numbers, A target integer
Aim: To find all possible unique quadruplets that sum up to target

Approach: 
- Sort the array
- Loop through the array till the third last element (As we need quadruplets and need minimum 3 elements more at this point)
    - Take current element of this loop as ele_1
    - Loop through the array from the next element of ele_1 to second last element (As we need atleast 2 more at this point)
        - Take the current element of this 2nd stage loop as ele_2
        - Sum ele_1 and ele_2 and store it as tempsum
        - Set left as index of next to ele_2 and right as the index of last element
        - Loop as long as left is less than right:
            - Sum the left element, right element and tempsum as finalsum
            - If finalsum equals target, add the list of elements as a tuple to finlist and increase left and decrease right both by 1
            - Else if lesser, increase left by 1
            - Else if greater, decrease right by 1
- Now we have a list of tuples of quadruplets that add up to the target
- Convert finlist to a set
- Convert finlist back to a list as we need to return a list and return it

What we did: 
- Sorted the array for easier processing
- Fixed 2 elements and utilised 2 pointer approach for the rest of the elements to efficiently determine quadruplets
- Gradually moved the fixed nums towards right, exploring all combinations while preventing redundancies
- Converted the final list to a set to remove duplicates 

Time Complexity: O(n^3)
'''