"""
You are given an integer num. You know that Bob will sneakily remap one of the 10 possible digits (0 to 9) to another digit.

Return the difference between the maximum and minimum values Bob can make by remapping exactly one digit in num.

Notes:

    When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences of d1 in num with d2.
    Bob can remap a digit to itself, in which case num does not change.
    Bob can remap different digits for obtaining minimum and maximum values respectively.
    The resulting number after remapping can contain leading zeroes.
"""


class Solution:
    def minMaxDifference(self, num: int) -> int:
        sn = str(num)
        max_num, min_num = [], []
        seen_max = sn[0] == "9"
        seen_min = sn[0] == "0"
        r_min, r_max = None, None

        for i in range(len(sn)):
            if sn[i] != "9" and not r_max:
                r_max = sn[i]
            if sn[i] != "0" and not r_min:
                r_min = sn[i]
            
            max_num.append("9" if sn[i] == r_max else sn[i])
            min_num.append("0" if sn[i] == r_min else sn[i])

        return abs(int("".join(max_num)) - int("".join(min_num)))
        
