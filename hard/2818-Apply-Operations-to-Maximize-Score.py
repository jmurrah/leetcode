"""
You are given an array nums of n positive integers and an integer k.

Initially, you start with a score of 1. You have to maximize your score by applying the following operation at most k times:

    Choose any non-empty subarray nums[l, ..., r] that you haven't chosen previously.
    Choose an element x of nums[l, ..., r] with the highest prime score. If multiple such elements exist, choose the one with the smallest index.
    Multiply your score by x.

Here, nums[l, ..., r] denotes the subarray of nums starting at index l and ending at the index r, both ends being inclusive.

The prime score of an integer x is equal to the number of distinct prime factors of x. For example, the prime score of 300 is 3 since 300 = 2 * 2 * 3 * 5 * 5.

Return the maximum possible score after applying at most k operations.

Since the answer may be large, return it modulo 109 + 7.
"""


class Solution:
    def getPrimeScore(self, original_num, prime_scores):
        if original_num in prime_scores:
            return prime_scores[original_num]
            
        score, num, seen = 0, original_num, set()
        while num % 2 == 0:
            if 2 not in seen:
                score += 1
                seen.add(2)
            num //= 2

        i = 3
        while i * i <= num:
            while num % i == 0:
                if i not in seen:
                    score += 1
                    seen.add(i)
                num //= i
            i += 2
        
        if num > 1:
            score += 1
        
        prime_scores[original_num] = score
        return score

    def maximumScore(self, nums: List[int], k: int) -> int:
        prime_scores = {}
        for num in nums:
            if num not in prime_scores:
                prime_scores[num] = self.getPrimeScore(num, prime_scores)

        stack, left = [], [-1] * len(nums)
        for i in range(len(nums)):
            score = prime_scores[nums[i]]
            while stack and stack[-1][0] < score:
                stack.pop()
            left[i] = stack[-1][1] if stack else -1
            stack.append((score, i))
        
        stack, right = [], [-1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            score = prime_scores[nums[i]]
            while stack and stack[-1][0] <= score:
                stack.pop()
            right[i] = stack[-1][1] if stack else len(nums)
            stack.append((score, i))

        heap = []
        for i in range(len(nums)):
            count = (i - left[i]) * (right[i] - i)
            heappush(heap, (-nums[i], count))
        
        score = 1
        MOD = 10 ** 9 + 7
        while k:
            num, count = heappop(heap)
            score = (score * pow(-num, min(count, k), MOD)) % MOD
            k -= min(count, k)
        
        return score
