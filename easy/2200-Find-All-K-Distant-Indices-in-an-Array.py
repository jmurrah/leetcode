"""
You are given a 0-indexed integer array nums and two integers key and k. A k-distant index is an index i of nums for which there 
exists at least one index j such that |i - j| <= k and nums[j] == key.

Return a list of all k-distant indices sorted in increasing order.
"""


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        keys = [i for i in range(len(nums)) if nums[i] == key]
        indicies = set(keys)

        for key in keys:
            l = key - 1
            while l >= 0 and l not in indicies and abs(l - key) <= k:
                indicies.add(l)
                l -= 1

            r = key + 1
            while r < len(nums) and r not in indicies and abs(r - key) <= k:
                indicies.add(r)
                r += 1
        
        return sorted(indicies)
