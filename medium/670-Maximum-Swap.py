"""
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        sn = list(str(num))
        stack = []

        for i, n in enumerate(sn):
            if not stack or n <= stack[-1][0]:
                stack.append((sn[i], i))
                continue

            mn, mi = "-", -1
            for j in range(i, len(sn)):
                if sn[j] >= mn:
                    mn, mi = sn[j], j

            pn, pi = None, None
            while stack and stack[-1][0] < mn:
                pn, pi = stack.pop()

            if pn:
                sn[pi], sn[mi] = sn[mi], sn[pi]
                return int("".join(sn))
        
        return num
            
