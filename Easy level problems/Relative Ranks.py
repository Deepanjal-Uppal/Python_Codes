# PROBLEM:

# You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

# The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. 
# The placement of each athlete determines their rank:

# The 1st place athlete's rank is "Gold Medal".
# The 2nd place athlete's rank is "Silver Medal".
# The 3rd place athlete's rank is "Bronze Medal".
# For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ith athlete.

 

# Example:

# Input: score = [5,4,3,2,1]
# Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
# Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].

# SOLUTION:

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        li = []

        for i in range(len(score)):
            li.append((score[i], i))

        answer = [0] * len(score)
        heapq.heapify(li)

        for i in range(len(li), 0, -1):
            value, pos = heapq.heappop(li)
            if i == 1:
                answer[pos] = "Gold Medal"
            elif i == 2:
                answer[pos] = "Silver Medal"
            elif i == 3:
                answer[pos] = "Bronze Medal"
            else:
                answer[pos] = str(i)

        return answer
