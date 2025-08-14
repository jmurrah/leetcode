"""
You are given a string num representing a large integer. An integer is good if it meets the following conditions:

    It is a substring of num with length 3.
    It consists of only one unique digit.

Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:

    A substring is a contiguous sequence of characters within a string.
    There may be leading zeroes in num or a good integer.
"""


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        output = ""
        for i in range(2, len(num)):
            if num[i-2] == num[i-1] == num[i] and (not output or num[i] > output[0]):
                output = num[i] * 3
        
        return output
        
