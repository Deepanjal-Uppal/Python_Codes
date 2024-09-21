# PROBLEM:

# Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

# You must write an algorithm that runs in O(n) time and uses O(1) extra space.  

# Example:

# Input: n = 13
# Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

# SOLUTION:

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        curr = 1

        while len(res) < n:
            res.append(curr)

            if curr * 10 <= n:
                curr *= 10
            else:
                while curr == n or curr % 10 == 9:
                    curr = curr // 10
                curr += 1
        
        return res
