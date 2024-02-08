from math import nan
from typing import Any


class ArrayQueue:
    DEFAULT_CAPACITY = 10  # moderate capacity for all new queues

    def __init__(self) -> None:
        # Createa a new empty queue
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._data == 0

    def first(self) -> Any:
        # Return but not remove first element
        if self.is_empty():
            print("Queue is empty")
            # return -1
        return self._data[self._front]

    def dequeue(self) -> Any:
        # Remove and return the first element of the queue FIFO
        if self.is_empty():
            print("Queue is empty")
            return -1
        val = self._data[self._front]
        self._data[self._front] = None  # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return val

    def enqueue(self, item) -> None:
        # Add an element to the back of the queue
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
            pass
        position = (self._front + self._size) % len(self._data)
        self._data[position] = item
        self._size += 1

    def _resize(self, cap) -> None:  # We assume cap >= len(self)
        # Resize to a new list of capacity >= len(self)
        old = self._data  # Keep track of existing list
        self._data = [None] * cap  # Allocate list with new capacity
        walk = self._front
        for k in range(self._size):  # Only consider existing elements
            self._data[k] = old[walk]  # Intentionally shift indices
            walk = (1 + walk) % len(old)  # Use old size as modulus
        self._front = 0  # Front has been realigned

    def __str__(self) -> str:
        ans: str = "["
        walk = self._front
        for k in range(self._size):
            # print(self._data[walk])
            if len(ans) > 1:
                ans += "->"
            ans += str(self._data[walk])
            walk = (1 + walk) % len(self._data)
        # walk = (1 + walk) % len(self._data)
        # ans += str(self._data[walk])
        ans += "]"
        return ans


def main():
    q = ArrayQueue()
    for i in range(10):
        # print(f"Inserting {i} into q")
        q.enqueue(i)
    print(f"Printing q: {q}")
    print(f"Printing first element: {q.dequeue()}")
    front = q.dequeue()
    print(front)
    print(q)
    front = q.dequeue()
    print(front)
    print(q)

    q.enqueue(100)
    print(q)
    q.enqueue(200)
    print(q)


if __name__ == "__main__":
    main()
