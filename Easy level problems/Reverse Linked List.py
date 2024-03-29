# PROBLEM:

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example:

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# SOLUTION:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
