# PROBLEM:

# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Example:

# Input: head = [1,2,2,1]
# Output: true

# SOLUTION:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow

        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        while prev != None:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        
        return True

        
