class Deque:
    def __init__(self):
        self._items = []

    def add_front(self, item):
        self._items.insert(0, item)

    def remove_front(self):
        return self._items.pop(0)

    def add_rear(self, item):
        self._items.append(item)

    def remove_rear(self):
        return self._items.pop()

    def is_empty(self):
        return not bool(self._items)

    def size(self):
        return len(self._items)

    def peek_front(self):
        return self._items[-1]

    def peek_rear(self):
        return self._items[0]

    def __str__(self):
        return str(self._items)


def str_to_deque(word):
    deque = Deque()
    for char in word:
        deque.add_rear(char)
    return deque


def palindrome_checker(word):
    deque_word = str_to_deque(word.lower())
    
    while deque_word.size() > 1:
        first = deque_word.remove_front()
        last = deque_word.remove_rear()
        if first != last:
            return False

    return True


print(palindrome_checker("lsdkjfskf"))
print(palindrome_checker("radar"))