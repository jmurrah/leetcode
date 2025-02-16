"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
"""


class Solution:
    def convertQueens(self, queens, n):
        converted = []
        for _, col in queens:
            converted.append("".join(["Q" if i == col else "." for i in range(n)]))
        return converted

    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, diag_pos, diag_neg = set(), set(), set()
        output = []

        def backtrack(r, queens):
            if len(queens) == n:
                output.append(self.convertQueens(queens, n))
                return
            if r == n:
                return

            for c in range(n):
                if (r + c) in diag_pos or (r - c) in diag_neg or c in cols:
                    continue

                cols.add(c)
                diag_pos.add(r + c)
                diag_neg.add(r - c)
                queens.append((r, c))

                backtrack(r + 1, queens)

                cols.remove(c)
                diag_pos.remove(r + c)
                diag_neg.remove(r - c)
                queens.pop()
        
        for r in range(n):
            backtrack(r, [])

        return output
