# PROBLEM:

# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. 
# If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Example:

# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]

# SOLUTION:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            curr = node
            i = 1

            while curr and i <= k:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                i += 1
            return prev, curr

        curr = head
        count = 0
        while curr:
            curr = curr.next
            count += 1

        turns = count // k
        dummy = ListNode(1)
        inc = dummy
        curr = head
        
        i = 1
        while curr and i <= turns:
            p, curr = reverse(curr)
            while inc.next:
                inc = inc.next
            inc.next = p
            i += 1
        
        if inc.next != None:
            while inc.next:
                inc = inc.next
            
        inc.next = curr

        return dummy.next
