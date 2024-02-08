from typing import Any


class Link(object):
    def __init__(self, data, next=None) -> None:
        self.__data: Any = data
        self.__next: Any = next

    def getData(self) -> Any:
        return self.__data

    def setData(self, data) -> None:
        self.__data = data

    def getNext(self) -> Any:
        return self.__next

    def setNext(self, link) -> None:
        if link is None or isinstance(link, Link):
            self.__next = link
        else:
            raise Exception("Next link must be link or None")

    def isLast(self) -> bool:
        return self.getNext() is None

    def __str__(self) -> str:
        return str(self.getData())


class LinkedList(object):
    def __init__(self) -> None:
        self.__first: Link = Link(None)

    def getFirst(self) -> Link:
        return self.__first

    def setFirst(self, link) -> None:
        if link is None or isinstance(link, Link):
            self.__first = link
        else:
            raise Exception("First link must be link or None")

    def getNext(self) -> Link:
        return self.getFirst()

    def setNext(self, link) -> None:
        self.setFirst(link)

    def isEmpty(self) -> bool:
        return self.getFirst() is None

    def first(self):
        if self.isEmpty():
            raise Exception("No first item in empty list")
        return self.getFirst.getData()

    def traverse(self, func=print):
        link = self.getFirst()
        while link is not None:
            func(link.getData())
            link = link.getNext()

    def __len__(self) -> int:
        l = 0
        link: Link = self.getFirst()
        while link is not None:
            l += 1
            link = link.getNext()

        return l

    def __str__(self) -> str:
        ans = "["
        link = self.getFirst()
        while link is not None:
            if len(ans) > 1:
                ans += "->"
            ans += str(link)
            link = link.getNext()
        ans += "]"
        return ans


def main() -> None:
    l1 = Link(1)
    l2 = Link(2)
    l3 = Link(3)

    l1.setNext(l2)
    l2.setNext(l3)

    ll = LinkedList()
    ll.setFirst(l1)
    # ll.setFirst(l2)
    # ll.setFirst(l3)
    ll.traverse()
    print("finished")
    print(ll)

    l4 = Link(4)
    ll.setFirst(l4)
    print(ll)


if __name__ == "__main__":
    main()
