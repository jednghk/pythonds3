'''
Implement stack abstract data type, which is collection of elements which follow a first in, last out
concept.
Methods to implement
1. push - takes in arg and adds to stack
2. is_empty - returns True or False
3. pop - removes first element of the stack and returns it
4. peek - returns first element of stack but does not remove it
5. size - returns number of elements in the stack
'''


class Stack:
    def __init__(self):
        self._items = []

    def push(self, elem):
        self._items.append(elem)

    def pop(self):
        return self._items.pop()

    def is_empty(self):
        return not bool(self._items)

    def peek(self):
        if not self.is_empty():
            return self._items[-1]

    def size(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)