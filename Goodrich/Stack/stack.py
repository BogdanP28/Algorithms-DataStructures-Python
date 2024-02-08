from typing import Any


# Implementing a stack using a python list


class ArrayStack:
    def __init__(self) -> None:
        self._data = []

    def __len__(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def push(self, item: Any) -> None:
        self._data.append(item)

    def pop(self) -> Any:
        if self.is_empty():
            # raise Empty("")
            print("Empty array")
            return None
        else:
            return self._data.pop()

    def peek(self) -> Any:
        if self.is_empty():
            # raise Empty("")
            print("Empty array")
            return None
        else:
            top = self._data[-1]
            return top

    def __str__(self) -> str:
        ans = "["
        for i in range(len(self._data)):
            if len(ans) > 1:
                ans += ", "
            ans += str(self._data[i])
        ans += "]"
        return ans


def is_matched_html(raw) -> bool:
    # Return True if all HTML tags are properrly match; False otherwise

    S = ArrayStack()
    j: int = raw.find("<")  # Find first "<" character (if any)
    while j != -1:
        k: int = raw.find(">", j + 1)  # Find next ">" (if any)
        if k == -1:
            return False  # Invalid tag
        tag: str = raw[j + 1 : k]  # Strip away <>
        if not tag.startswith("/"):  # This is opening tag
            S.push(tag)
        else:
            if S.is_empty():
                return False  # Nothing to match with
            tmp: str = S.pop()
            tmp: str = tmp.split(" ")[0]
            if tag[1:] != tmp:
                return False  # Mismatched delimiter
        j = raw.find("<", k + 1)  # find next "<" if any
    return S.is_empty()


def main2():
    f = open("Goodrich/test.html", "r")
    raw = ""
    text = f.readlines()
    for line in text:
        raw += line
    print(is_matched_html(raw))


def main() -> None:
    nrItems = 5
    stack = ArrayStack()
    for i in range(nrItems):
        print(f"Pushing: {i}")
        stack.push(i)
    print(f"Printing stack: {stack}")
    print(f"Pushing: {6}")
    stack.push(6)
    print(f"Printing stack: {stack}")
    print(f"Peeking stack: {stack.peek()}")
    print(f"Popping: {stack.pop()}")
    print(f"Peeking stack: {stack.peek()}")
    print(f"Printing stack: {stack}")
    print(f"Popping: {stack.pop()}")
    print(f"Popping: {stack.pop()}")
    print(f"Popping: {stack.pop()}")
    print(f"Peeking stack: {stack.peek()}")
    print(f"Popping: {stack.pop()}")
    print(f"Peeking stack: {stack.peek()}")


if __name__ == "__main__":
    # main()
    main2()
