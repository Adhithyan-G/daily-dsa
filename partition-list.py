# 86. Partition List

'''
Question:
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        leftHead = None
        left = None
        rightHead = None
        right = None
        temp = head
        while(temp):
            print(temp.val)
            if temp.val < x:
                if not leftHead:
                    leftHead = temp
                else:
                    left.next = temp
                left = temp
            else:
                if not rightHead:
                    rightHead = temp
                else:
                    right.next = temp
                right = temp
            temp = temp.next
        if right:
            right.next = None
        if left:
            left.next = rightHead
            return leftHead
        return head

'''
Explanation:
Given: The head of a singly linked list and a value x
Aim: Partition the list such that all nodes < x come before nodes >= x, preserving relative order

Approach:
- Early exit if list is empty
- Initialize leftHead, left, rightHead and right as None
- We will maintain order in the leftHead's list with elements < x and the rest in rightHead's list 
- Set temp as head
- While temp is not None:
    - If value of temp is less than x:
        - If leftHead is not already initialized:
            - Set leftHead as temp (first element less than x)
        - Else set next element in left as temp
        - Update left as temp 
    - Else:
        - If rightHead is not already initialized:
            - Set rightHead as temp (first element not less than x)
        - Else set next element in right as temp
        - Update right as temp 
    - Set temp as temp.next to continue traversing the list
- Break any next link from right and set it as None to avoid cicular references
- If left exists (the linked list had atleast one element less than x), Connect rightHead to left and return leftHead
- Return head when no element less than x was present.
'''