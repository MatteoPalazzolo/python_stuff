from __future__ import annotations
from typing import Any, Self

class LinkedList:
    class Node:
        def __init__(self, value: Any, next: LinkedList.Node|None = None):
            self._value: Any = value
            self._next: LinkedList.Node|None = next

        def get_value(self) -> Any:
            return self._value
        
        def set_value(self, value: Any):
            self._value = value

        def get_next(self) -> LinkedList.Node|None:
            return self._next

        def set_next(self, next: LinkedList.Node|None):
            self._next = next

        def __str__(self) -> str:
            return str(self._value)

    def __init__(self):
        self._len: int = 0
        self._start: LinkedList.Node|None = None

    def __len__(self) -> int:
        return self._len

    def insert_front(self, value: Any) -> Self:
        self._len += 1
        self._start = LinkedList.Node(value, self._start)
        return self

    def insert(self, idx: int, value: Any) -> Self:
        if idx < 0 or idx > self._len:
            raise IndexError("list index out of range")
        if idx == 0:
            self.insert_front(value)
            return self
        if not self._start: #typechecker stuff
            raise Exception()
        
        self._len += 1
        node = self._start
        for _ in range(idx-1):
            node = node.get_next() if node else None
        if node:
            node.set_next(LinkedList.Node(value,node.get_next()))

        return self

    def remove(self, idx: int) -> Self:
        if idx < 0 or idx >= self._len:
            raise IndexError("list index out of range")
        if not self._start: #typechecker stuff
            raise Exception()
        
        self._len -= 1
        prvs: LinkedList.Node|None = None
        node: LinkedList.Node|None = self._start
        for _ in range(idx):
            prvs = node
            node = node.get_next() if node else None

        next = node.get_next() if node else None
        if prvs:
            prvs.set_next(next)
        else:
            self._start = next

        return self

    def __getitem__(self, idx: int) -> Any:
        if idx < 0 or idx >= self._len:
            raise IndexError("list index out of range")
        
        node: LinkedList.Node|None = self._start
        for _ in range(idx):
            node = node.get_next() if node else None
        if node is None: #typechecker stuff
            raise Exception()
        return node.get_value()

    def __setitem__(self, idx: int, value: Any):
        if idx < 0 or idx >= self._len:
            raise IndexError("list index out of range")
        
        node: LinkedList.Node|None = self._start
        for _ in range(idx):
            node = node.get_next() if node else None
        if node is None: #typechecker stuff
            raise Exception()
        
        node.set_value(value)

    def __repr__(self) -> str:
        node: LinkedList.Node|None = self._start
        if node is None:
            return "[]"
        out = "["
        for i in range(self._len):
            out += str(node)
            if i != self._len - 1:
                out += ", "
            node = node.get_next() if node else None
        return out + "]"


def main():
    lista = LinkedList()

    lista.insert_front("H")     # [H]
    lista.insert_front("F")     # [F, H]
    lista.insert_front("D")     # [D, F, H]
    print(lista, len(lista))

    lista.insert(0, "C")            # [C, D, F, H]
    lista.insert(2, "E")            # [C, D, E, F, H]
    lista.insert(len(lista), "I")   # [C, D, E, F, H, I]
    print(lista, len(lista))

    lista.remove(0)             # [D, E, F, H, I]
    lista.remove(2)             # [D, E, H, I]
    lista.remove(len(lista)-1)  # [D, E, H]
    print(lista, len(lista))

    print(lista[0], lista[1], lista[len(lista)-1])
    
    lista[0] = "X"  # [X, E, H]
    lista[1] = "Y"  # [X, Y, H]
    lista[2] = "Z"  # [X, Y, Z]
    print(lista)


if __name__ == "__main__":
    main()