"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go 
outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""


class Solution:
    def reverse(self, x: int) -> int:
        positive, x, ans = x >= 0, abs(x), 0
        
        while x:
            ans = (ans * 10) + (x % 10)
            x //= 10
        
        if not positive:
            ans = -ans

        return ans if -2**31 < ans < 2**31 else 0
