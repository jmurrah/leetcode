"""
Given a positive integer n, return the punishment number of n.

The punishment number of n is defined as the sum of the squares of all integers i such that:

    1 <= i <= n
    The decimal representation of i * i can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals i.

"""


class Solution:
    def punishmentNumber(self, n: int) -> int:
        def backtrack(sn, curr, target):
            if not sn:
                return curr == target

            return backtrack(sn[1:], int(sn[0]), target - curr) or backtrack(
                sn[1:], curr * 10 + int(sn[0]), target
            )

        p_num = 0
        for num in range(1, n + 1):
            if backtrack(str(num * num), 0, num):
                p_num += num * num

        return p_num
