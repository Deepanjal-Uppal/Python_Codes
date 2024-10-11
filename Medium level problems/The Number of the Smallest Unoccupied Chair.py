# PROBLEM:

# There is a party where n friends numbered from 0 to n - 1 are attending. 
# There is an infinite number of chairs in this party that are numbered from 0 to infinity. 
# When a friend arrives at the party, they sit on the unoccupied chair with the smallest number.

# For example, if chairs 0, 1, and 5 are occupied when a friend comes, they will sit on chair number 2.
# When a friend leaves the party, their chair becomes unoccupied at the moment they leave. 
# If another friend arrives at that same moment, they can sit in that chair.

# You are given a 0-indexed 2D integer array times where times[i] = [arrivali, leavingi], 
# indicating the arrival and leaving times of the ith friend respectively, and an integer targetFriend. All arrival times are distinct.

# Return the chair number that the friend numbered targetFriend will sit on.

# Example:

# Input: times = [[1,4],[2,3],[4,6]], targetFriend = 1
# Output: 1
# Explanation: 
# - Friend 0 arrives at time 1 and sits on chair 0.
# - Friend 1 arrives at time 2 and sits on chair 1.
# - Friend 1 leaves at time 3 and chair 1 becomes empty.
# - Friend 0 leaves at time 4 and chair 0 becomes empty.
# - Friend 2 arrives at time 4 and sits on chair 0.
# Since friend 1 sat on chair 1, we return 1.

# SOLUTION:

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        available = [n for n in range(0, len(times))]
        heapq.heapify(available)
        unavailable = [] #leaving, chair
        new_times = []
        friend = 0
        for arrival, leaving in times:
            new_times.append([arrival, leaving, friend])
            friend += 1

        new_times.sort()

        for arrival, leaving, friend in new_times:
            while len(unavailable) > 0 and unavailable[0][0] <= arrival:
                _, chair = heapq.heappop(unavailable)
                heapq.heappush(available, chair)
            else:
                chair = heapq.heappop(available)
            if friend == targetFriend:
                return chair
            heapq.heappush(unavailable, (leaving, chair))

        return -1

    
