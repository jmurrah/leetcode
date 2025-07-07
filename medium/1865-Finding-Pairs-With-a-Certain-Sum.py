"""
You are given two integer arrays nums1 and nums2. You are tasked to implement a data structure that supports queries of two types:

    Add a positive integer to an element of a given index in the array nums2.
    Count the number of pairs (i, j) such that nums1[i] + nums2[j] equals a given value (0 <= i < nums1.length and 0 <= j < nums2.length).

Implement the FindSumPairs class:

    FindSumPairs(int[] nums1, int[] nums2) Initializes the FindSumPairs object with two integer arrays nums1 and nums2.
    void add(int index, int val) Adds val to nums2[index], i.e., apply nums2[index] += val.
    int count(int tot) Returns the number of pairs (i, j) such that nums1[i] + nums2[j] == tot.
"""


class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.n1 = nums1
        self.n2 = nums2
        self.c = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.c[self.n2[index]] -= 1
        if not self.c[self.n2[index]]:
            del self.c[self.n2[index]]

        self.n2[index] += val
        self.c[self.n2[index]] += 1

    def count(self, tot: int) -> int:
        total = 0
        for n in self.n1:
            if tot - n in self.c:
                total += self.c[tot - n]
        return total

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
