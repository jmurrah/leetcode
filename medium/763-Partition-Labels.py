"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. 
For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.
"""


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count, output, i = Counter(s), [], 0
        
        while i < len(s):
            seen, start = set([s[i]]), i
            while seen:
                seen.add(s[i])
                count[s[i]] -= 1
                if count[s[i]] == 0:
                    seen.remove(s[i])
                i += 1
            output.append(i - start)
        
        return output
