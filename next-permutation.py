# 31. Next Permutation
'''
Question: 
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.
'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        swap=-1
        size=len(nums)
        for i in range(size-1, 0, -1):
            if(nums[i]>nums[i-1]):
                swap=i-1
                break
        if(swap==-1):
            for j in range(0,size//2):
                nums[j], nums[-j-1] = nums[-j-1], nums[j]
            return
        for i in range(size-1, 0, -1):
            if(nums[i]>nums[swap]):
                nums[swap], nums[i] = nums[i], nums[swap]
                break
        revrange=(size-swap-1)//2
        for i in range(1,revrange+1):
            nums[-i], nums[swap+i] = nums[swap+i], nums[-i]
        return

'''
Explanation:
Given: An array of integers
Aim: To change the elements of array in place such the resulting array is the next greater number possible to form by appending the numbers in order after the number that would have been formed by appending the numbers in the original given array.
Example: [1,2,3] -> 123 and next number would be 132 -> [1,3,2]

Approach:
- We initialize the swapping index as -1 and get the size of the array
- To achieve the very next greater number, we would want to change the least affecting places which would change the value of the number ones->tens->hundreds and so on
- We check from the right to left, where the value of the integer is greater than that of its left and assign swap index as the index of the left element
- After complete checking if swap is still -1, Then it means the array is in non-ascending  order and hence would be forming the greatest number possible as is. In this case we reverse the array to get it in non-decreasing order to be forming the smallest number possible as the next one should be circularly in order
- If swap has a valid index, We look for the integer that is greater than it again in the smallest value affecting order and swap them
- After swapping, We reverse everything after the swap index to end to minimise the value as that range would be in a non-increasing order
- Hence, We would have effectively changed the array to form the next number when merged by changing their values in place and using constant memory!
'''