# PROBLEM:

# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, 
# plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. 
# Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.

# Example:

# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), 
# all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

# SOLUTION:

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = deque([])
        queue.append((sr, sc))
        initial_color = image[sr][sc]

        while len(queue) > 0:
            r, c = queue.popleft()
            if image[r][c] == initial_color:
                image[r][c] = color
            
            direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for row, col in direction:
                new_r, new_c = r + row, c + col
                if new_r < 0 or new_r >= len(image) or new_c < 0 or new_c >= len(image[0]) or image[new_r][new_c] != initial_color or image[new_r][new_c] == color:
                    continue
                queue.append((new_r, new_c))

        return image
