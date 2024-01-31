
from typing import Any
class Stack(object):
    def __init__(self, max: int) -> None:
        self.__stackList = [None] * max
        self.__top = -1
        
    def push(self, item: Any) -> None: 
        self.__top += 1
        if not self.isFull():
            self.__stackList[self.__top] = item
        else:
            self.__top -= 1
            print("Stack is full!")
            
    def pop(self):
        top: Any = self.__stackList[self.__top]
        self.__stackList[self.__top] = None
        self.__top -= 1
        return top
    
    def peek(self) -> Any:
        if not self.isEmpty():
            return self.__stackList[self.__top]
        else:
            print("Empty Array")
            return None
        
        
    def isEmpty(self) -> bool:
        return self.__top < 0
    
    def isFull(self) -> bool:
        return self.__top >= len(self.__stackList)
    
    def __len__(self) -> int:
        return len(self.__stackList)
    
    def __str__(self) -> str:
        ans = "["
        for i in range(self.__top + 1):
            if len(ans) > 1:
                ans += ", "
            ans += str(self.__stackList[i])
        ans += "]"
        return ans
    
def main() -> None:
    nrItems = 5
    stack = Stack(nrItems)
    for i in range(nrItems):
        stack.push(i)
    print(stack)
    stack.push(6)
    print(stack.peek())
    stack.pop()
    print(stack.peek())
    print(stack)
    stack.pop()
    stack.pop()
    stack.pop()
    print(stack.peek())
    stack.pop()
    print(stack.peek())

    
    
if __name__ == '__main__':
    main()