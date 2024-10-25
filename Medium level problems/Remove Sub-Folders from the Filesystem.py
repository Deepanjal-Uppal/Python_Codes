# PROBLEM:

# Given a list of folders folder, return the folders after removing all sub-folders in those folders. 
# You may return the answer in any order.

# If a folder[i] is located within another folder[j], it is called a sub-folder of it. 
# A sub-folder of folder[j] must start with folder[j], followed by a "/". 
# For example, "/a/b" is a sub-folder of "/a", but "/b" is not a sub-folder of "/a/b/c".

# The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.

# For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.
 
# Example:

# Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
# Output: ["/a","/c/d","/c/f"]
# Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.

# SOLUTION:

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = [folder[0]]

        for i in range(1, len(folder)):
            last_folder = res[-1] + '/'
            if not folder[i].startswith(last_folder):
                res.append(folder[i])
        return res
