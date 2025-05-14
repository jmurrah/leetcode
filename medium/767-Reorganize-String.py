"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.
"""


class Solution:
    def reorganizeString(self, s: str) -> str:
        h = [(-v, k) for k, v in Counter(s).items()]
        heapify(h)

        output = ["IGNORE"]
        while h:
            inv_v, k = heappop(h)
            if k == output[-1]:
                if not h:
                    return ""
                next_inv_v, next_k = heappop(h)
                output.append(next_k)
                heappush(h, (inv_v, k))
                if next_inv_v + 1 < 0:
                    heappush(h, (next_inv_v + 1, next_k))
            else:
                output.append(k)
                if inv_v + 1 < 0:
                    heappush(h, (inv_v + 1, k))

        return "".join(output[1:])
