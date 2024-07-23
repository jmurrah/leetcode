"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
  string convert(string s, int numRows);
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        output = []
        for r in range(numRows):
            i = r
            while i < len(s):
                output.append(s[i])
                i += (numRows - 1) * 2
                if 0 < r < numRows - 1:
                    if i - (2 * r) < len(s):
                        output.append(s[i - (2 * r)])
        
        return "".join(output)
