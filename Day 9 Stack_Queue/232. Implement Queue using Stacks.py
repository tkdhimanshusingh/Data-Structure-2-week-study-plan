class MyQueue:

    def __init__(self):
        self._items = []
        

    def push(self, x: int) -> None:
        self._items.append(x)
        

    def pop(self) -> int:
        return self._items.pop(0)
        

    def peek(self) -> int:
        return self._items[0]
        

    def empty(self) -> bool:
        return not bool(self._items)