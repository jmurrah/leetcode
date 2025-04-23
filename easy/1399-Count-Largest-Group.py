"""
You are given an integer n.

Each number from 1 to n is grouped according to the sum of its digits.

Return the number of groups that have the largest size.
"""


class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = defaultdict(int)
        count = length = 0
        for num in range(1, n+1):
            s = sum([int(d) for d in str(num)])
            groups[s] += 1

            if groups[s] == length:
                count += 1
            elif groups[s] > length:
                length = groups[s]
                count = 1
        
        return count
