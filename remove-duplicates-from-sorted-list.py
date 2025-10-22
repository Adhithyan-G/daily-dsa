# 83. Remove Duplicates from Sorted List

'''
Question:
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head):
            return None
        temp = head.next
        last = head
        while(temp):
            if temp.val != last.val:
                last.next = temp
                last = temp
            temp = temp.next
        last.next = None
        return head

'''
Given: A sorted linked list where duplicate values may appear consecutively.
Aim: Remove duplicates so that each element appears only once, maintaining the sorted order.

Approach:
- If the list is empty, return None immediately.
- Initialize temp as the second node and last as the first node (head).
- Traverse the list while temp is not None:
    - If the current node's value (temp.val) differs from the last unique node's value (last.val):
        - Link last.next to temp to include this distinct value.
        - Move last forward to this new unique node.
    - Move temp to the next node
- After traversal, set last.next = None to disconnect any residual duplicate links.
- Return the head of the deduplicated linked list.
'''