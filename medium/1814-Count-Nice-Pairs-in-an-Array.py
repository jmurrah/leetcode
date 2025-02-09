"""
You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the 
non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it 
satisfies all of the following conditions:

    0 <= i < j < nums.length
    nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])

Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.
"""


class Solution:
    def __init__(self):
        self.rev_nums = {}

    def rev(self, num):
        if num in self.rev_nums:
            return self.rev_nums[num]

        n, output = num, 0
        while n:
            output = output * 10 + (n % 10)
            n //= 10

        self.rev_nums[num] = output
        return output

    def countNicePairs(self, nums: List[int]) -> int:
        targets = defaultdict(int)
        for i in range(len(nums)):
            targets[nums[i] - self.rev(nums[i])] += 1

        good = 0
        for v in targets.values():
            good += v * (v - 1) // 2
        
        return good % (10 ** 9 + 7)
