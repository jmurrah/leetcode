"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys 
exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
"""


class ListNode:
    def __init__(self, k=0, v=0, p=None, n=None):
        self.key = k
        self.val = v
        self.prev = p
        self.next = n

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.map = {}

        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_front(self, node):
        self.remove_node(node)
        self.add_to_front(node)

    def add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.move_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.move_to_front(node)
        else:
            new_node = ListNode(k=key, v=value)
            self.map[key] = new_node
            self.add_to_front(new_node)
            self.size += 1
            if self.size > self.capacity:
                lru = self.tail.prev
                self.remove_node(lru)
                del self.map[lru.key]
                self.size -= 1
