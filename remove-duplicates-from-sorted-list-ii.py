# 82. Remove Duplicates from Sorted List II

'''
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        skipThis = False
        last = None
        head = None
        while(temp):
            curval = temp.val
            skipThis = False
            while(temp.next and temp.next.val == curval):
                skipThis = True
                temp = temp.next
            if not skipThis:
                if last:
                    last.next = temp
                    last = last.next
                else:
                    last = temp
                    head = temp
            temp = temp.next
        if last:
            last.next = None
        return head

'''
Given: A sorted linked list non decreasing order where nodes with duplicate values may appear consecutively

Aim: Remove any nodes that appear more than once and keep only nodes that are unique in the entire list
- Return the head of the resulting linked list

Approach:
- Initialize a temp variable as head which we will use to traverse through the linked list 
- Set skipThis as False which will indicate whether to skip the current node from the new list
- Reset head and set last (which will finally denote the last node) as None

- While temp (current node) is not Null:
    - Store its value as curval.
    - Move forward while next nodes have the same value 
        - Mark duplicates as skipThis = True.
    - If the current value is not a duplicate:
        - Append it to the new chain using last pointer.
        - Move last pointer to the last node currently
        - Update head if it's the first valid node.
    - Move temp to its next.
- After traversal, ensure last.next = None to break any leftover links.
- Return the head of the new filtered list.
'''