# PROBLEM:

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Example:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# SOLUTION:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        li = []
        def helper(i):
            curr = i
            while curr != None:
                li.append(curr.val)
                curr = curr.next

        for i in lists:
            helper(i)

        li.sort()

        res = ListNode(0)
        ans = res

        for i in li:
            new = ListNode(i)
            ans.next = new
            ans = ans.next

        return res.next        
