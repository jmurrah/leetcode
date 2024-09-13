"""
Reverse bits of a given 32 bits unsigned integer.

Note:

    Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output 
    will be given as a signed integer type. They should not affect your implementation, as the integer's internal 
    binary representation is the same, whether it is signed or unsigned.
    In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, 
    the input represents the signed integer -3 and the output represents the signed integer -1073741825.

"""


class Solution:
    def reverseBits(self, n: int) -> int:
        if n == 0:
            return 0
            
        binary = ["0"] * 32
        curr = n
        for i in range(math.floor(math.log(n, 2)), -1, -1):
            if curr >= 2 ** i:
                binary[i] = "1"
                curr -= 2 ** i

        output = 0
        for i, num in enumerate(binary[::-1]):
            if num == "1":
                output += 2 ** i
        
        return output
