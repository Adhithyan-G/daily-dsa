# 21. Merge Two Sorted Lists

'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1):
            return list2
        if (not list2):
            return list1
        if (list1.val>list2.val):
            list1, list2=list2, list1
        final_head=list1
        while(list1.next and list2):
            if((list1.next).val>list2.val):
                list1.next, list2=list2, list1.next
            list1=list1.next
        if list2:
            list1.next=list2
        return final_head

'''
Explanation: 
Given: Head node of two linked lists sorted in non-decreasing order
Aim: To merge the lists into one list in non-descending order and return merged list head

Approach: 
- First, if either of lists or empty, We return the other list head as final merged list's head
- We set list1's head node to be lesser or equal to the list2's head node
- We set the list1's head node as final head node as we know it has the smallest value of the two lists now
- We loop until list1 does not have a next element or list2 has been completely traversed
    - If the value of next node of list1 is greater than list2's value, We set list2 as next node of list1 and list2 as the originally next node of current list1, So that list1's last processed value stays not greater than list2's value
    - We set list1 as the current next node of list1
- After the loop ends, We check If list2 still exists, If yes, We set list2 as list1's next as list1's current value will not be greater than list2's value and list2 is still sorted
- We return the merged sorted list's head which is the original list1's head

Time complexity: O(n) where n is the length of the merged list
'''