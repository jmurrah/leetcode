"""
You are given an integer array digits, where each element is a digit. The array may contain duplicates.

You need to find all the unique integers that follow the given requirements:

    The integer consists of the concatenation of three elements from digits in any arbitrary order.
    The integer does not have leading zeros.
    The integer is even.

For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.

Return a sorted array of the unique integers.
"""


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = Counter(digits)
        output = set()

        def combine(cnt, curr):
            if len(curr) == 3:
                if int(curr[-1]) % 2 == 0:
                    output.add(int("".join(curr)))
                return

            for k in cnt.keys():
                if not curr and k == 0:
                    continue
                temp = cnt.copy()
                temp[k] -= 1
                if temp[k] == 0:
                    del temp[k]
                combine(temp, curr + [str(k)])
        
        combine(count, [])
        return sorted(list(output))
      
