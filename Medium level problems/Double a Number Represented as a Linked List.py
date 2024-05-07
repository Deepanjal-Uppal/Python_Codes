# PROBLEM:

# You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

# Return the head of the linked list after doubling it.

# Example:

# Input: head = [1,8,9]
# Output: [3,7,8]
# Explanation: The figure above corresponds to the given linked list which represents the number 189. 
# Hence, the returned linked list represents the number 189 * 2 = 378.

# SOLUTION:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            curr = head
            prev = None

            while curr != None:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        curr = reverse(head)
        ans = curr
        carry = 0

        while curr != None:
            temp = (curr.val * 2) + carry
            if temp > 0:
                carry = temp // 10
                rem = temp % 10
                curr.val = rem
            else:
                curr.val = temp

            curr = curr.next

        res = reverse(ans)

        if carry != 0:
            new = ListNode(carry, None)
            new.next = res
            return new
        else:
            return res
