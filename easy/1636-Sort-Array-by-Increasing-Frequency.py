"""
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. 
If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.
"""


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        groups, output = defaultdict(list), []

        for k, v in Counter(nums).items():
            groups[v].append(k)

        for k, l in sorted(groups.items(), key=lambda g: g[0]):
            for n in sorted(l, reverse=True):
                output.extend([n]*k)

        return output
