# 24. Swap Nodes in Pairs

'''
Question: 
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node1=head
        if(node1):
            node2=head.next
        else: 
            return head
        if (node2):
            head=node2
        while(node1 and node2):
            nextpair=[node2.next, (node2.next.next if node2.next else None)]
            node1,node2=node2,node1
            node2.next=(nextpair[0] if not nextpair[1] else nextpair[1])
            node1.next=node2
            node1=nextpair[0]
            node2=nextpair[1]
        return head

'''
Explanation:
Given: A Head node of a linked List
Aim: To Swap the position of every set of adjacent pairs of nodes not their values

Approach:
- Set node1 as head
- If no node exists, return head which is None else set node2 as head's next
- If node2 exists, set head as node2 as it would be the head after swapping
- While node1 and node2 exist, 
    - Store the next pair of nodes to be swapped before swapping the current pair
    - Swap node1 and node2
    - Just because we swapped them their next nodes wouldn't be swapped!
    - Set the next node of node2 as the seccond node in the nextpair as it would be swapped
    - Set the node2 as the next node of node1
    - Loop with reassiging the next pair to node1 and node2
- Now all nodes have been successfully swapped, return the set head node
'''