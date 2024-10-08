"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
"""


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []

        for num in range(1, n + 1):
            if num % 3 == 0 and num % 5 == 0:
                output.append("FizzBuzz")
            elif num % 3 == 0:
                output.append("Fizz")
            elif num % 5 == 0:
                output.append("Buzz")
            else:
                output.append(str(num))
        
        return output
