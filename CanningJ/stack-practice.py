from typing import Any


class Stack(object):
    def __init__(self, max: int) -> None:
        self.__stackList: list[Any] = [None] * max
        self.__top = -1

    def push(self, item) -> None:
        self.__top += 1
        if not self.isFull():
            self.__stackList[self.__top] = item
        else:
            print("Stack is full")
            self.__top -= 1

    def isFull(self) -> bool:
        return self.__top >= len(self.__stackList)

    def isEmpty(self) -> bool:
        return self.__top < 0

    def __len__(self) -> int:
        return self.__top + 1

    def __str__(self) -> str:
        ans: str = "["
        for i in range(self.__top + 1):
            if len(ans) > 1:
                ans += ","
            ans += str(self.__stackList[i])
        ans += "]"

        return ans


def main() -> None:
    size: int = 5
    stack = Stack(size)
    for i in range(size):
        stack.push(i)
    print(stack)
    stack.push(6)
    print(stack)


if __name__ == "__main__":
    main()
