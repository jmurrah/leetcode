"""
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = [str(n) for n in range(1, 10)]
        output = []

        i = 0
        while i < len(pattern):
            if pattern[i] == "I":
                output.append(stack.pop(0))
                i += 1
                continue

            d = 0
            while (i + d) < len(pattern) and pattern[i + d] == "D":
                d += 1
            
            for j in range(d, 0, -1):
                output.append(stack.pop(j))

            i += d
        
        output.append(stack[0])
        return "".join(output)
"""


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = [str(n) for n in range(1, 10)]
        output = []

        i = 0
        while i < len(pattern):
            if pattern[i] == "I":
                output.append(stack.pop(0))
                i += 1
                continue

            d = 0
            while (i + d) < len(pattern) and pattern[i + d] == "D":
                d += 1
            
            for j in range(d, 0, -1):
                output.append(stack.pop(j))

            i += d
        
        output.append(stack[0])
        return "".join(output)
