"""
Write a function that takes the binary representation of a positive integer and returns the number of
set bits it has (also known as the Hamming weight).
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        for i in range(math.floor(math.log(n, 2)), -1, -1):
            if n >= 2 ** i:
                n -= 2 ** i
                count += 1
        
        return count
