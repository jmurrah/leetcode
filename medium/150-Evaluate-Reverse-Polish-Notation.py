"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""


class Solution:
    def perform_operation(self, n2, n1, operation):
        if operation == "+":
            return n1 + n2
        elif operation == "-":
            return n1 - n2
        elif operation == "*":
            return n1 * n2
        elif operation == "/":
            return n1 / n2

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] in "+-*/":
                stack.append(self.perform_operation(int(stack.pop()), int(stack.pop()), tokens[i]))
            else:
                stack.append(tokens[i])
        
        return int(stack[0])
