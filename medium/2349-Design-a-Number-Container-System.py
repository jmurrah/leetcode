"""
Design a number container system that can do the following:

    Insert or Replace a number at the given index in the system.
    Return the smallest index for the given number in the system.

Implement the NumberContainers class:

    NumberContainers() Initializes the number container system.
    void change(int index, int number) Fills the container at index with the number. If there is already a number at that index, replace it.
    int find(int number) Returns the smallest index for the given number, or -1 if there is no index that is filled by number in the system.
"""


class NumberContainers:

    def __init__(self):
        self.numbers = {}
        self.indexes = {}
        
    def change(self, index: int, number: int) -> None:
        self.indexes[index] = number
        if number not in self.numbers:
            h = []
            heapify(h)
            self.numbers[number] = h
        heappush(self.numbers[number], index)

    def find(self, number: int) -> int:
        if number not in self.numbers:
            return -1

        heap = self.numbers[number]
        while heap:
            smallest_index = heap[0]
            if self.indexes[smallest_index] == number:
                return smallest_index
            heappop(heap)
        
        return -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
