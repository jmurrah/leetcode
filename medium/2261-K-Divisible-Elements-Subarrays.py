"""
Given an integer array nums and two integers k and p, return the number of distinct subarrays, which have at most k elements that are divisible by p.

Two arrays nums1 and nums2 are said to be distinct if:

    They are of different lengths, or
    There exists at least one index i where nums1[i] != nums2[i].

A subarray is defined as a non-empty contiguous sequence of elements in an array.
"""


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        output = []
        
        for i in range(len(nums)):
            current, count = [], 0
            for j in range(i, len(nums)):
                if nums[j] // p == nums[j] / p:
                    count += 1
                
                if not count > k:
                    current.append(nums[j])
                else:
                    break
                    
                output.append(tuple(current))
                    
        return len(set(output))
