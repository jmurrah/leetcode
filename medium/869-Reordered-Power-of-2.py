"""
You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.
"""


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        powers = set()
        for p in range(32):
            num = 2 ** p
            powers.add(tuple(sorted(str(num))))
        
        return tuple(sorted(str(n))) in powers
