"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d, count, out = {}, {}, []

        for i in nums:
            count[i] = count.get(i, 0) + 1

        for n, c in count.items():
            if not d.get(c):
                d[c] = [n]
            elif n not in d[c]:
                d[c].append(n)
        
        c = 0
        for i in range(len(nums), -1, -1):
            for j in d.get(i, []):
                out.append(j)
                c += 1
                if c == k:
                    return out
