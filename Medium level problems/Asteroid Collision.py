# PROBLEM:

# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, 
# and the sign represents its direction (positive meaning right, 
# negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. 
# If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. 
# Two asteroids moving in the same direction will never meet.

# Example:

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

# SOLUTION:

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        i=0

        while i in range(0,len(asteroids)):
            if len(st) == 0:
                st.append(asteroids[i])
                i+=1
            elif asteroids[i] > 0:
                st.append(asteroids[i])
                i+=1
            elif asteroids[i] < 0:
                top = st[-1]
                if top < 0 and asteroids[i] < 0:
                    st.append(asteroids[i])
                    i+=1
                elif abs(top) == abs(asteroids[i]):
                    st.pop()
                    i+=1
                elif abs(top) > abs(asteroids[i]):
                    i+=1
                else:
                    st.pop()
                    pass
        return st

