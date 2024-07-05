# PROBLEM:

# A critical point in a linked list is defined as either a local maxima or a local minima.

# A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.

# A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.

# Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.

# Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] 
# where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points.
# If there are fewer than two critical points, return [-1, -1].

# Example:

# Input: head = [3,1]
# Output: [-1,-1]
# Explanation: There are no critical points in [3,1].

# SOLUTION:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if head.next == None or head.next.next == None:
            return [-1, -1]

        prev = head
        curr = head.next
        after = head.next.next
        mini = float('inf')
        i = 2
        first = 0
        critical1 = 0
        critical2 = 0

        while after != None:
            if (prev.val > curr.val and after.val > curr.val) or (prev.val < curr.val and after.val < curr.val):
                if first == 0:
                    critical1 = i
                    critical2 = i
                else:
                    mini = min(mini, i - critical2)
                    critical2 = i
                first += 1

            i += 1
            prev = prev.next
            curr = curr.next
            after = after.next

        if mini == float('inf') and critical2 - critical1 == 0:
            return [-1, -1]
        
        return [mini, critical2 - critical1]
