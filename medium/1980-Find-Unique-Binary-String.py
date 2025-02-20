"""
Given an array of strings nums containing n unique binary strings each of length n, return a binary string 
of length n that does not appear in nums. If there are multiple answers, you may return any of them.
"""


class Solution:
    def convertNumToBinary(self, n, length):
        binary = []
        for i in range(length-1, -1, -1):
            if n >= 2 ** i:
                binary.append("1")
                n -= 2 ** i
            else:
                binary.append("0")
        return "".join(binary)

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        curr, length = 0, len(nums[0])

        for num in sorted(nums):
            curr_binary = self.convertNumToBinary(curr, length)
            if curr_binary != num:
                return curr_binary

            curr += 1
        
        return self.convertNumToBinary(curr, length)
