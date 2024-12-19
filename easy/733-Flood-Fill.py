"""
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. 
You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the
pixel image[sr][sc].

To perform a flood fill:

    Begin with the starting pixel and change its color to color.
    Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, 
    either horizontally or vertically) and shares the same color as the starting pixel.
    Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches 
    the original color of the starting pixel.
    The process stops when there are no more adjacent pixels of the original color to update.

Return the modified image after performing the flood fill.
"""


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        original_color = image[sr][sc]
        dq = deque([(sr, sc)])
        
        while dq:
            for i in range(len(dq)):
                row, col = dq.pop()
                if 0 <= row < len(image) and 0 <= col < len(image[0]) and image[row][col] == original_color:
                    image[row][col] = color
                    dq.appendleft((row+1, col))
                    dq.appendleft((row-1, col))
                    dq.appendleft((row, col+1))
                    dq.appendleft((row, col-1))
        
        return image
