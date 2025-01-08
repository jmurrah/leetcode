"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.
"""


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1
        
        max_heap = []
        heapq.heapify(max_heap)
        for word, count in word_count.items():
            heapq.heappush(max_heap, (-count, word))
        
        k_most_frequent_words = []
        while k > 0:
            k_most_frequent_words.append(heapq.heappop(max_heap)[1])
            k -= 1
        
        return k_most_frequent_words
