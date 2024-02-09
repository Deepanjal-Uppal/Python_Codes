# PROBLEM:

# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Example:

# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

# SOLUTION:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        res = dummy = ListNode(0)
        dummy.next = head

        while head:
            if head.val == val:
                dummy.next = head.next
                head = head.next
            else:
                dummy = dummy.next
                head = head.next

        return res.next
