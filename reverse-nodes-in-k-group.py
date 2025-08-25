# 25. Reverse Nodes in k-Group

'''
Question: 

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        headNotSet=True
        stack=list()
        i=0
        node=head
        lastNode=None
        while(node):
            i+=1
            nextNode=node.next
            if(i==k):
                if(headNotSet):
                    head=node
                    headNotSet=False
                if(lastNode):
                    lastNode.next=node
                while(stack):
                    node.next=stack.pop()
                    node=node.next
                lastNode=node
                i=0
            else:
                stack.append(node)
            node=nextNode
        lastNode.next=stack[0] if stack else None
        return head
'''
Explanation:

- Given: Head of a linked list, and a integer k
- Aim: To reverse every set of k nodes in the linked list (not their values)

Approach:
- Initiate a stack to keep track of the nodes for each k nodes
- Set node as head node and integer i as 0 to keep count
- While node exists, 
    - Increase i by 1 to denote the ith node of the set is being processed
    - Set nextNode as the next node
    - If i==k, It means we have a set complete.
        - If head node was not changed already, set head node to current node as we'll reverse this set and this will be the first node
        - If there was a set before this, We set that set's lastnode's next as current node to properly connect the sets
        - We pop the stack assigning every node's next as the next node popped from the stack
        - When all nodes are popped, We set the last node popped as the lastnode to be used for the next set and reset count (i) as 0
    - Else We add the node to the stack and move on to the next node
- We set the next node of LastNode as 0th element of stack if stack exists indicating there were leftover elements not enough to form a set thus unreversed else we set it to None
- We return the set head node of the modified Linked List
'''