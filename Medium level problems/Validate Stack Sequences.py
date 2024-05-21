# PROBLEM:

# Given two integer arrays pushed and popped each with distinct values, 
# return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

# Example:

# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4),
# pop() -> 4,
# push(5),
# pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

# SOLUTION:

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []

        popped_ptr = 0
        for i in pushed:
            st.append(i)
            while popped_ptr < len(popped) and len(st) > 0 and st[-1] == popped[popped_ptr]:
                st.pop()
                popped_ptr += 1
        
        if len(st) == 0:
            return True
        else:
            return False
