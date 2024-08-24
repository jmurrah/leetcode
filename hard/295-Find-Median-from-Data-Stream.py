"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, 
and the median is the mean of the two middle values.

    For example, for arr = [2,3,4], the median is 3.
    For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the data structure.
    double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

"""


class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heappush(self.large, num)
        else:
            heappush(self.small, -num)

        if len(self.small) - len(self.large) == 2:
            heappush(self.large, -heappop(self.small))
        if len(self.large) - len(self.small) == 2:
            heappush(self.small, -heappop(self.large))


    def findMedian(self) -> float:
        total = len(self.small) + len(self.large)
        if total % 2 == 1:
            return -self.small[0] if len(self.small) > len(self.large) else self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2
        
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
