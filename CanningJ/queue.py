from operator import itemgetter
from typing import Any


class Queue(object):
    def __init__(self, size: int) -> None:  # Constructor
        self.__maxSize: int = size  # Size of [circular] array
        self.__que: list[Any] = [None] * size  # Queue stored as a list
        self.__front: int = 1  # Empty queue has front 1
        self.__rear: int = 0
        self.__nItems: int = 0  # No items in queue

    def insert(self, item: int) -> None:
        if self.isFull():
            raise Exception("Queue overflow")

        self.__rear += 1
        if self.__rear == self.__maxSize:
            self.__rear = 0
        self.__que[self.__rear] = item
        self.__nItems += 1

    def remove(self) -> int:
        if self.isEmpty():
            raise Exception("Queue overflow")
        front: int = self.__que[self.__front]
        self.__que[front] = None
        self.__front += 1
        if self.__front == self.__maxSize:
            self.__front = 0
        self.__nItems -= 1
        return front

    def isEmpty(self) -> bool:
        return self.__nItems == 0

    def isFull(self) -> bool:
        return self.__nItems == self.__maxSize

    def __len__(self) -> int:
        return self.__nItems

    def __str__(self):
        ans = "["
        for i in range(self.__nItems):
            if len(ans) > 1:
                ans += ", "
            j = i + self.__front
            if j >= self.__maxSize:
                j -= self.__maxSize
            ans += str(self.__que[j])
        ans += "]"
        return ans


def main() -> None:
    q = Queue(10)
    size = 10
    for i in range(size):
        q.insert(i)
    print(q)

    front = q.remove()
    print(front)
    print(q)
    front = q.remove()
    print(front)
    print(q)

    q.insert(100)
    print(q)
    q.insert(200)
    print(q)


if __name__ == "__main__":
    main()
