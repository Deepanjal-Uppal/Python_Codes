# PROBLEM:

# Given the head of a singly linked list and two integers left and right where left <= right, 
# reverse the nodes of the list from position left to position right, and return the reversed list.

# Example:

# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]

# SOLUTION:

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)

        leftprev = dummy
        curr = head
        for i in range(left - 1):
            leftprev = curr
            curr = curr.next

        prev = None
        for i in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        leftprev.next.next = curr
        leftprev.next = prev

        return dummy.next
