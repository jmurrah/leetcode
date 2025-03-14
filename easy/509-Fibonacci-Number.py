"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each 
number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).
"""


class Solution:
    def fib(self, n: int) -> int:
        seen = {}
        
        def fibonacci(num):
            if num < 2:
                return num
            if num in seen:
                return seen[num]

            seen[num] = fibonacci(num - 1) + fibonacci(num - 2)
            return seen[num]

        return fibonacci(n)
