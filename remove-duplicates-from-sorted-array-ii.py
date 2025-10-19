# 80. Remove Duplicates from Sorted Array II

'''
Question:
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        target = 2
        for i in range(2,len(nums)):
            nums[target] = nums[i]
            if not (nums[target] == nums[target-1] == nums[target-2]):
                target += 1
        return target

'''
Explanation:  
Given: A sorted integer array nums (non-decreasing order).  
Aim: Modify nums in-place so that each unique number appears at most twice, returning the new valid length.  

Approach:  
- Since the array is sorted, all duplicates are grouped together — we can easily detect them by checking consecutive elements.  
- Use a variable `target` to represent the next position where a valid number can be placed.  
- Base case:  
    - If nums has 2 or fewer elements, return its length directly as all are valid.  
- Start iterating from index 2 (since the first two elements are always allowed).  
    - For each nums[i], assign nums[target] = nums[i].  
    - Then check if the last three elements (nums[target], nums[target-1], nums[target-2]) are equal.  
        - If not all three are the same -> this is a valid placement -> increment target.  
        - If all three are same -> we have a triple duplicate -> skip increment (effectively overwriting later).  
- After traversal, (target) will represent the count of valid elements as it points to the index we would have modified next denoting everything until it fulfils the condition. 
'''