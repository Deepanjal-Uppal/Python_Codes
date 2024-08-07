# PROBLEM:

# The Leetcode file system keeps a log each time some user performs a change folder operation.

# The operations are described below:

# "../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
# "./" : Remain in the same folder.
# "x/" : Move to the child folder named x (This folder is guaranteed to always exist).
# You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

# The file system starts in the main folder, then the operations in logs are performed.

# Return the minimum number of operations needed to go back to the main folder after the change folder operations.

# Example:

# Input: logs = ["d1/","d2/","../","d21/","./"]
# Output: 2
# Explanation: Use this change folder operation "../" 2 times and go back to the main folder.

# SOLUTION:

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0

        for i in logs:
            if i == "../":
                if res > 0:
                    res -= 1
            elif i =="./":
                pass
            else:
                res += 1
        return res
