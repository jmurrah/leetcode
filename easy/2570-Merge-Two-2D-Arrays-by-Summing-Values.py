"""
You are given two 2D integer arrays nums1 and nums2.

    nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
    nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.

Each array contains unique ids and is sorted in ascending order by id.

Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

    Only ids that appear in at least one of the two arrays should be included in the resulting array.
    Each id should be included only once and its value should be the sum of the values of this id in the two arrays. 
    If the id does not exist in one of the two arrays, then assume its value in that array to be 0.

Return the resulting array. The returned array must be sorted in ascending order by id.
"""


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        output = []
        i1 = i2 = 0
        len1, len2 = len(nums1), len(nums2)

        while i1 < len1 or i2 < len2:
            if i1 < len1 and i2 < len2 and nums1[i1][0] == nums2[i2][0]:
                output.append([nums1[i1][0], nums1[i1][1] + nums2[i2][1]])
                i1 += 1
                i2 += 1
            elif not i2 < len2 or (i1 < len1 and nums1[i1][0] < nums2[i2][0]):
                output.append(nums1[i1])
                i1 += 1
            else:
                output.append(nums2[i2])
                i2 += 1
        
        return output
                
