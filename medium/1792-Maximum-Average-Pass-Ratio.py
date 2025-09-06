"""
There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. 
You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.

You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. 
You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.

The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. 
The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.
"""


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h = [] # increase, pass, total
        for p, t in classes:
            increase = (p + 1) / (t + 1) - p/t
            heappush(h, (-increase, p, t))

        while extraStudents > 0:
            inc, p, t = heappop(h)
            p += 1
            t += 1
            increase = (p + 1) / (t + 1) - p/t
            heappush(h, (-increase, p, t))
            extraStudents -= 1
        
        total = 0
        while h:
            i, p, t = heappop(h)
            total += p / t
        
        return total / len(classes)
