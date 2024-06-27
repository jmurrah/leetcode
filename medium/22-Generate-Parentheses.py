"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def add_parenthesis(current, open_count, closed_count):
            if open_count == closed_count == n:
                output.append(current)
                return
            if open_count < n:
                add_parenthesis(current + "(", open_count + 1, closed_count)
            if closed_count < open_count:
                add_parenthesis(current + ")", open_count, closed_count + 1)
        
        add_parenthesis("", 0, 0)
        return output
