"""
You are given a string number representing a positive integer and a character digit.

Return the resulting string after removing exactly one occurrence of digit from number such that the value of the resulting 
string in decimal form is maximized. The test cases are generated such that digit occurs at least once in number.
"""


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_number = 0

        for i, element in enumerate(number):
            if element == digit:
                max_number = max(int(number[:i] + number[i+1:]), max_number)

        return str(max_number)
