# PROBLEM:

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example:

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# SOLUTION:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr = temp = ListNode()

        curr1 = list1
        curr2 = list2

        while curr1 != None and curr2 != None:
            if curr1.val <= curr2.val:
                curr.next = curr1
                curr1 = curr1.next
                curr = curr.next
            else:
                curr.next = curr2
                curr2 = curr2.next
                curr = curr.next
        
        if curr1 == None or curr2 ==None:
            if curr1 ==None:
                curr.next = curr2
            else:
                curr.next = curr1

        return temp.next
