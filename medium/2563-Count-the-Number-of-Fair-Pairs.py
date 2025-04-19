"""
Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

    0 <= i < j < n, and
    lower <= nums[i] + nums[j] <= upper

"""


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        def search(target):
            count = 0
            l, r = 0, len(nums) - 1
            while l < r:
                num = nums[l] + nums[r]
                if num > target:
                    r -= 1
                else:
                    count += r - l
                    l += 1

            return count

        return search(upper) - search(lower - 1)
