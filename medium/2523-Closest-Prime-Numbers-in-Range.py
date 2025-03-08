"""
Given two positive integers left and right, find the two integers num1 and num2 such that:

    left <= num1 < num2 <= right .
    Both num1 and num2 are prime numbers.
    num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.

Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].
"""


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = [0, 0] + [1] * (right - 1)
        for num in range(2, int(right**0.5) + 1):
            if not sieve[num]:
                continue
            offset = num + num
            while offset < right + 1:
                sieve[offset] = 0
                offset += num

        primes = [n for n in range(len(sieve)) if sieve[n] and n >= left]
        closest = [float("-inf"), float("inf")]
        for i in range(1, len(primes)):
            if primes[i] - primes[i-1] < closest[1] - closest[0]:
                closest = [primes[i-1], primes[i]]

        return closest if closest[0] != float("-inf") else [-1, -1]
