from typing import Any


class ArrayQueue(object):
    def __init__(self, size: int) -> None:
        self.__q: list[Any] = [None] * size
        self.__size: int = size
        self.__front: int = 0
        self.__nrItems: int = 0

    def enqueue(self, item: int) -> None:
        if self.isFull():
            raise Exception("Queue overflow!")
        position: int = (self.__front + self.__nrItems) % self.__size
        self.__q[position] = item
        self.__nrItems += 1

    def isFull(self) -> bool:
        return self.__nrItems == self.__size

    def isEmpty(self) -> bool:
        return self.__nrItems == 0

    def __len__(self) -> int:
        return self.__nrItems

    def dequeue(self) -> int:
        if self.isEmpty():
            raise Exception("Empty queue")
        frontPosition: int = (self.__front + self.__nrItems) % self.__size
        front = self.__q[frontPosition]
        self.__q[frontPosition] = None
        self.__front += 1
        self.__nrItems -= 1
        return front

    def __str__(self) -> str:
        ans = ""
        ans += "TO DO"
        return ans


class Queue(object):
    def __init__(self, size: int) -> None:
        self.__q: list[Any] = [None] * size
        self.__size: int = size
        self.__front = 1
        self.__rear = 0
        self.__nrItems = 0

    def enqueue(self, item: int) -> None:
        if self.isFull():
            raise Exception("Queue overflow!")

        self.__rear += 1
        if self.__rear == self.__size:
            self.__rear = 0
        self.__q[self.__rear] = item
        self.__nrItems += 1

    def dequeue(self) -> int:
        if self.isEmpty():
            raise Exception("Queue is empty!")
        front = self.__q[self.__front]
        self.__q[self.__front] = None
        self.__front += 1
        self.__nrItems -= 1
        return front

    def isEmpty(self) -> bool:
        return self.__nrItems == 0

    def isFull(self) -> bool:
        return self.__nrItems == self.__size

    def __len__(self) -> int:
        return self.__nrItems

    def __str__(self) -> str:
        ans = "["
        for i in range(self.__nrItems):
            if len(ans) > 1:
                ans += "->"
            j = i + self.__front
            if j >= self.__size:
                j -= self.__size
            ans += str(self.__q[j])
        ans += "]"
        return ans


def main():
    q = ArrayQueue(10)
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


def main2() -> None:
    q = Queue(10)
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
    main2()
