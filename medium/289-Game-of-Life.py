"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by 
the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). 
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population.
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. 
Given the current state of the m x n grid board, return the next state.
"""


class Solution:
    def get_number_live_neighbors(self, board: List[List[int]], x: int, y: int) -> int:
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (0 <= x + i < len(board) and 0 <= y + j < len(board[0]) and board[x + i][y + j] == 1):
                    if not (i == j == 0):
                        count += 1
        return count

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        live_neighbors = {}

        for i in range(len(board)):
            for j in range(len(board[i])):
                live_neighbors[(i, j)] = {
                    "number": board[i][j],
                    "count": self.get_number_live_neighbors(board, i, j),
                }

        for i in range(len(board)):
            for j in range(len(board[i])):
                if (live_neighbors[(i, j)]["number"] != 1 and live_neighbors[(i, j)]["count"] == 3):
                    board[i][j] = 1
                elif live_neighbors[(i, j)]["number"] == 1 and live_neighbors[(i, j)]["count"] not in [2, 3]:
                    board[i][j] = 0
