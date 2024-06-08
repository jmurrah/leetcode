"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, box = defaultdict(set), defaultdict(set), defaultdict(set)

        for i in range(9):
            for j in range(9):
                number = board[i][j]
                if number == ".":
                    continue

                if number in row[i] or number in col[j] or number in box[(i // 3, j // 3)]:
                    return False

                row[i].add(number)
                col[j].add(number)
                box[(i // 3, j // 3)].add(number)

        return True
