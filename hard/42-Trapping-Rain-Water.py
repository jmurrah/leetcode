"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        output = 0
        l, r = 0, len(height) - 1
        mhl, mhr = height[0], height[len(height)-1]
        
        while l < r:
            if mhl < mhr:
                l += 1
                mhl = max(mhl, height[l])
                output += mhl - height[l]
            else:
                r -= 1
                mhr = max(mhr, height[r])
                output += mhr - height[r]

        return output
