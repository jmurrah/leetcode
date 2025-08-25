"""
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
"""


class Solution:
    # NOTE: d = 1 (up) or 0 (down)
    def getDiagonal(self, mat, r, c, d):
        diag = []
        while 0 <= r < len(mat) and 0 <= c < len(mat[0]):
            diag.append(mat[r][c])
            if d == 1:
                r -= 1
                c += 1
            else:
                r += 1
                c -= 1
        
        return diag

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ups = []
        # get up diags
        for r in range(0, len(mat), 2):
            ups.append(self.getDiagonal(mat, r, 0, 1))
        for c in range(1 + (len(mat) % 2), len(mat[0]), 2):
            ups.append(self.getDiagonal(mat, len(mat)-1, c, 1))
        
        downs = []
        # get down diags
        for c in range(1, len(mat[0]), 2):
            downs.append(self.getDiagonal(mat, 0, c, 0))
        for r in range(1 + int(len(mat[0]) % 2 == 0), len(mat), 2):
            downs.append(self.getDiagonal(mat, r, len(mat[0])-1, 0))

        u = d = 0
        output = []
        while u < len(ups):
            if u < len(ups):
                output.extend(ups[u])
                u += 1
            if d < len(downs):
                output.extend(downs[d])
                d += 1
        
        return output
