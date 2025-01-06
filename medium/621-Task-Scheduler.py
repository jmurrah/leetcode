"""
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. 
Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.
"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_left = Counter(tasks)
        max_heap = []
        heapq.heapify(max_heap)

        for k, v in tasks_left.items():
            heapq.heappush(max_heap, (-v, k))

        number_intervals = 0
        dq = deque()

        while tasks_left:
            number_intervals += 1
            if dq and dq[-1][0] == number_intervals:
                _, letter, count = dq.pop()
                heapq.heappush(max_heap, (-count, letter))

            if not max_heap:
                continue

            _, letter = heapq.heappop(max_heap)
            tasks_left[letter] -= 1
            if tasks_left[letter] == 0:
                del tasks_left[letter]
                continue

            dq.appendleft((number_intervals + n + 1, letter, tasks_left[letter]))
        
        return number_intervals
        
