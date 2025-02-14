"""
Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.

Implement the ProductOfNumbers class:

    ProductOfNumbers() Initializes the object with an empty stream.
    void add(int num) Appends the integer num to the stream.
    int getProduct(int k) Returns the product of the last k numbers in the current list. You can assume that always the current list has at least k numbers.

The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.
"""


class ProductOfNumbers:
    def __init__(self):
        self.products = []

    def add(self, num: int) -> None:
        if num == 0:
            self.products = []
        elif not self.products:
            self.products.append(num)
        else:
            self.products.append(self.products[-1] * num)

    def getProduct(self, k: int) -> int:
        if k > len(self.products):
            return 0
        elif k == len(self.products):
            return self.products[-1]
        else:
            return self.products[-1] // self.products[-1-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
