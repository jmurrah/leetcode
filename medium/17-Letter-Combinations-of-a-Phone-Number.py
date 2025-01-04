"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        num_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        output = []

        def backtrack(i, curr):
            if i == len(digits):
                output.append("".join(curr))
                return
            
            for letter in num_map[digits[i]]:
                curr.append(letter)
                backtrack(i + 1, curr)
                curr.pop()
        
        backtrack(0, [])
        return output
