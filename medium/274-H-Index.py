"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, 
return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given 
researcher has published at least h papers that have each been cited at least h times.
"""


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        output = count = 0

        for i in range(len(citations)-1, -1 ,-1):
            count += 1
            if citations[i] >= count:
                output = max(output, count)
            
        return output
