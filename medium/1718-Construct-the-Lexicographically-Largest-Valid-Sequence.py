"""
Given an integer n, find a sequence that satisfies all of the following:

    The integer 1 occurs once in the sequence.
    Each integer between 2 and n occurs twice in the sequence.
    For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.

The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.

Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, 
sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than 
[0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.
"""


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        output = [0] * ((n - 1) * 2 + 1)
        seen = set()

        def find_valid(i):
            if i == len(output):
                return True
            if output[i] != 0:
                return find_valid(i + 1)

            for num in range(n, 0, -1):
                if num in seen or (
                    num != 1 and (i + num >= len(output) or output[i + num] != 0)
                ):
                    continue

                output[i] = num
                if num != 1:
                    output[i + num] = num

                seen.add(num)
                if find_valid(i + 1):
                    return True

                seen.remove(num)
                output[i] = 0
                if num != 1:
                    output[i + num] = 0

            return False

        find_valid(0)
        return output
