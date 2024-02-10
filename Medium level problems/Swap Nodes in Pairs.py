# PROBLEM:

# Given a linked list, swap every two adjacent nodes and return its head. 
# You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Example:

# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

# SOLUTION:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head

        prev = head
        curr = head.next

        while curr:
            prev.val, curr.val = curr.val, prev.val
            if curr.next and curr.next.next:
                prev = curr.next
                curr = prev.next
            else:
                return head 
        return head
