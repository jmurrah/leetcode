"""
You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

A uni-value grid is a grid where all the elements of it are equal.

Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.
"""


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        for row in grid:
            nums.extend(row)
        
        check = nums[0] % x
        if not all([num % x == check for num in nums]):
            return -1
        
        nums.sort()
        m1, m2 = nums[len(nums) // 2], nums[len(nums) // 2 - 1]
        c1 = sum([abs(num - m1) // x for num in nums])
        c2 = sum([abs(num - m2) // x for num in nums])

        return min(c1, c2)
