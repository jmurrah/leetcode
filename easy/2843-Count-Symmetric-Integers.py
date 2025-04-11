"""
You are given two positive integers low and high.

An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal to the sum of the last n digits of x. 
Numbers with an odd number of digits are never symmetric.

Return the number of symmetric integers in the range [low, high].
"""


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        output = 0
        for num in range(low, high+1):
            snum = str(num)
            len_num = len(snum)
            if len_num % 2 == 1: continue

            left = sum([int(d) for d in snum[:len_num//2]])
            right = sum([int(d) for d in snum[-len_num//2:]])
            output += int(left == right)
        
        return output
