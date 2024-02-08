from typing import Any


class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next: Any = next

    def __str__(self) -> str:
        return str(self.data)


class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.tail: Node = self.head

    def get(self, index: int) -> int: ...

    def addAtHead(self, val: int) -> None:
        """ """
        newNode = Node(val)
        newNode.next = self.head.next
        self.head.next = newNode
        while newNode.next:
            self.tail = newNode.next
            newNode = newNode.next
        print("here")

    def removeFrontElements(self, nr: int) -> None:
        idx = 0
        curr: Node = self.head
        while curr and idx <= nr:
            curr = curr.next
            idx += 1
        self.head.next = curr

    def addAtTail(self, val: int) -> None: ...

    def addAtIndex(self, index: int, val: int) -> None: ...

    def deleteAtIndex(self, index: int) -> None: ...

    def __str__(self) -> str:
        ans = "["
        curr: Node = self.head.next
        while curr:
            if len(ans) > 1:
                ans += "->"
            ans += str(curr)
            curr = curr.next
        ans += "]"
        return ans

    def printTail(self) -> str:
        return str(self.tail)

    def printHead(self) -> str:
        return str(self.head.next)


def main() -> None:
    # Your MyLinkedList object will be instantiated and called as such:
    obj = MyLinkedList()
    nrElements = 5
    for i in range(nrElements):
        obj.addAtHead(i)
    print(obj)
    print(f"tail is: {obj.printTail()}")
    print(f"head is: {obj.printHead()}")
    print("Removing front {nr} elements")
    obj.removeFrontElements(nrElements)
    print(obj)
    # param_1 = obj.get(index)
    # obj.addAtTail(9)
    # obj.addAtHead(1)
    # obj.addAtHead(2)
    # print("here")
    # obj.addAtTail(val)
    # obj.addAtIndex(index,val)
    # obj.deleteAtIndex(index)


if __name__ == "__main__":
    main()
