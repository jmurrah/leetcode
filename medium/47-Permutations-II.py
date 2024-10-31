"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output, d = [], {}

        for num in nums:
            d[num] = d.get(num, 0) + 1

        def permute(curr, d):
            if not d:
                output.append(curr)
                return
            
            for k in d:
                c = d.copy()
                c[k] -= 1
                if c[k] == 0: del c[k]
                permute(curr + [k], c)

        permute([], d)
        return output
