# 19. Remove Nth Node From End of List

'''
Question: 
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size=0
        temp=head
        while(temp):
            temp=temp.next
            size+=1
        if size==1:
            return None
        if size==n:
            return head.next
        temp=head
        n=size-n
        curr=0
        while(temp):
            if (curr==(n-1)):
                temp.next=temp.next.next
                return head
            temp=temp.next
            curr+=1

'''
Explanation: 
Given: Head of linked list, (n) position of number to remove from the last
Aim: To remove the nth element from the last

Approach: 
- Traverse through Linked list to find its size
- If size was 1, only that element can be removed so return None
- If size is equal to n, Last element from last which is the first element so return head.next
- set n as difference between size and n to find its position from the start
- Now that we know the element to remove from the start, traverse through the list and check whether the next element is the element to be removed for each element
- When hit, set the next element of the current element as the next element of the actual element effectively dropping the element to be removed and return head.
'''