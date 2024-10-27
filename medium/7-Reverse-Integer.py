"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go 
outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""


class Solution:
    def reverse(self, x: int) -> int:
        sx, zc = list(str(x)), 0
        pre = "-" if sx[0] == "-" else ""
        length = len(sx)

        if length == 1 or (length == 2 and pre):
            return x

        i = length
        while i <= 0 and sx[i] == "0":
            zc += 1
            i -= 1

        sx = sx[1:length-zc] if pre else sx[:length-zc]
        output = int("".join([pre] + sx[::-1]))
        return output if -math.pow(2, 31) < output < math.pow(2, 31) else 0
