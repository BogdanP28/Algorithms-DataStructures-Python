from typing import Any

class LinkedList:
    
    class _Node:
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next=None) -> None:
            self._element: Any = element
            self._next = next
            
    def __init__(self) -> None:
        self._head: Any = None
        self._size: int = -1
        
    def __len__(self) -> int:
        return self._size
    
    def isEmpty(self) -> bool:
        return self._size == 0
    
    def push(self, element) -> None:
        newElement = self._Node(element)
        newElement._next = self._head
        self._size += 1
        
    def top(self) -> Any:
        if self.isEmpty(): raise Exception("Empty stack")
        return self._head._element
        
    def pop(self) -> Any:
        if self.isEmpty(): raise Exception("Empty stack")
        top_element = self._head.element()
        self._head = self._head._next
        self._size -= 1
        return top_element
    
def main() -> None:
    stack = LinkedList()
    nrElements = 5
    for i in range(5):
        stack.push(i)
    print("here")