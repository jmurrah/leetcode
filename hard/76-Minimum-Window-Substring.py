"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every 
character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        correct_count, current_count = Counter(t), defaultdict(int)
        letters_needed, min_length = len(correct_count), float("inf")

        l = r = 0
        while r < len(s):
            right_char = s[r]
            if right_char in correct_count:
                current_count[right_char] += 1
                if current_count[right_char] == correct_count[right_char]:
                    letters_needed -= 1
            
            r += 1

            while letters_needed == 0:
                current_length = r - l
                if current_length < min_length:
                    min_length = current_length
                    output = s[l:r]

                left_char = s[l]
                if left_char in correct_count:
                    current_count[left_char] -= 1
                    if current_count[left_char] < correct_count[left_char]:
                        letters_needed += 1

                l += 1
        
        return output if min_length != float("inf") else ""
