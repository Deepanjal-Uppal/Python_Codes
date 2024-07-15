# PROBLEM:

# You are given an array of integers nums and the head of a linked list. 
# Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.

# Example:

# Input: nums = [1,2,3], head = [1,2,3,4,5]

# Output: [4,5]

# Explanation: Remove the nodes with values 1, 2, and 3.

# SOLUTION:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        prev = res
        curr = head
        nums = set(nums)

        while curr != None:
            if curr.val not in nums:
                prev.next = curr
                prev = prev.next
            else:
                prev.next = None
            curr = curr.next
            

        return res.next
