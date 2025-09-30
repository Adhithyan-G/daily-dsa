# 61. Rotate List

'''
Question:
Given the head of a linked list, rotate the list to the right by k places.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        temp = head
        n=1
        while(temp.next):
            temp=temp.next
            n=n+1
        k=k%n
        lastnode=temp
        lastnode.next=head
        temp=head
        for i in range(0, n-k-1):
            if(temp):
                temp=temp.next
        head = temp.next
        temp.next = None
        return head

'''
Explanation:
Given: Head of a singly linked list and integer k
Aim: Rotate the linked list to the right by k positions

Approach:
- If list is empty, has only one node, or k is 0 → directly return head (no rotation needed)
- Initialize temp as head and traverse till end to find length n
- Reduce k to its modulo n (k = k % n) since rotating n times brings list back to original
- Connect last node’s next to head (makes the list circular temporarily)
- Reset temp = head
- Move temp forward (n - k - 1) steps → temp now points to node just before new head
- Update head = temp.next (this is the new head after rotation)
- Break the circle by setting temp.next = None as current temp would be the last node
- Return head
'''