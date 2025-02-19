"""
A happy string is a string that:

    consists only of letters of the set ['a', 'b', 'c'].
    s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).

For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.
"""


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.k_happy = ""
        self.count = 0

        def find_k_happy(s):
            if len(s) == n:
                self.count += 1
                if self.count == k:
                    self.k_happy = "".join(s)
                return self.count == k
            
            for c in "abc":
                if not s or c != s[-1]:
                    s.append(c)
                    if find_k_happy(s):
                        return True
                    s.pop()

            return False
        
        find_k_happy([])
        return self.k_happy
