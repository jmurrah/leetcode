"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many 
times as it shows in both arrays and you may return the result in any order.
"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n2_count = Counter(nums2)
        output, d = [], defaultdict(int)

        for num in nums1:
            d[num] += 1
            if d[num] <= n2_count[num]:
                output.append(num)

        return output
