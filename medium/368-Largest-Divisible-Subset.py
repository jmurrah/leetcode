"""
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

    answer[i] % answer[j] == 0, or
    answer[j] % answer[i] == 0

If there are multiple solutions, return any of them.
"""


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        largest = (1, 0)
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] > largest[0]:
                        largest = (dp[i], i)
        
        output = []
        size, num = largest[0], nums[largest[1]]
        for i in range(largest[1], -1, -1):
            if size == dp[i] and num % nums[i] == 0:
                output.append(nums[i])
                num = nums[i]
                size -= 1

        return output
