"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are 
horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        len_row, len_col = len(board), len(board[0])

        def dfs(r, c, i, char_locations):
            if i == len(word):
                return True
            if (
                not 0 <= r < len_row
                or not 0 <= c < len_col
                or (r, c) in char_locations
                or board[r][c] != word[i]
            ):
                return False

            char_locations.add((r, c))
            i += 1

            result = (
                dfs(r - 1, c, i, char_locations)
                or dfs(r + 1, c, i, char_locations)
                or dfs(r, c - 1, i, char_locations)
                or dfs(r, c + 1, i, char_locations)
            )
            char_locations.remove((r, c))
            return result

        for r in range(len_row):
            for c in range(len_col):
                if dfs(r, c, 0, set()):
                    return True

        return False
