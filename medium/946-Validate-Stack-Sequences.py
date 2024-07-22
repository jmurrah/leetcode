"""
Given two integer arrays pushed and popped each with distinct values, return true if this could have been the 
result of a sequence of push and pop operations on an initially empty stack, or false otherwise.
"""


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, s = 0, []

        for push in pushed:
            s.append(push)
            while s and i < len(popped) and s[-1] == popped[i]:
                i += 1
                s.pop()
            
        return not s
