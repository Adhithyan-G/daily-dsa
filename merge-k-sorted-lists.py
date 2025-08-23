# 23. Merge k Sorted Lists

'''
Question: 

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergetwolists(list1, list2):
            n1 = len(list1)
            n2 = len(list2)
            if (n1==0 and n2==0):
                return None
            if (n1==0):
                return list2[0] if n2==1 else mergetwolists(list2[0:n2//2], list2[n2//2:n2])
            if (n2==0):
                return list1[0] if n1==1 else mergetwolists(list1[0:n1//2], list1[n1//2:n1])
            head1=list1[0]
            head2=list2[0]
            if (n1>1 or n2>1):
                head1=mergetwolists(list1[0:n1//2], list1[n1//2:n1])
                head2=mergetwolists(list2[0:n2//2], list2[n2//2:n2])
            if (head1==None):
                return head2
            if (head2==None):
                return head1 
            if (head1.val>head2.val):
                head1, head2 = head2, head1
            merged_head = head1
            while (head1.next and head2):
                if ((head1.next).val>head2.val):
                    head1.next, head2 = head2, head1.next
                head1=head1.next
            if (head2):
                head1.next=head2
            return merged_head
        
        k=len(lists)
        return mergetwolists(lists[0:k//2], lists[k//2:k])

'''
Explanation: 
Given: A list of sorted linked lists (Technically a list of head nodes of sorted linked lists)
Aim: To Merge all linked lists into one and return head of the merged linked list

Approach: 
- We define a helper function to handle the merging of two sorted linked lists
- The helper function takes 2 two lists of linked lists and recursively breaks each list down to 2 lists where each contain atmost one linked list
    - If Both are empty, We return None
    - If one of the lists is empty, We check the other list: 
        - Size of other list is 1, we return the first and only head node in the list
        - If not, We further break it down to divide it so that we can process it
    - If Both lists have more than one head node, We break down each list into smaller lists to merge
    - If both have only one head node, We merge the linked lists by traversing through them and splicing the nodes
    - After merging, We return the merged linked list's head node. ending the helper function
- We split the given list of linked lists into two and sart processing recursively using the above defined helper function which would ultimately return the complete merged linked list's head
'''