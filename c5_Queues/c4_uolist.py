class Node:
    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, node_data):
        self._data = node_data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_node):
        self._next = next_node


class UnorderedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add(self, node_data):
        temp = Node(node_data)
        temp.next = self.head
        self.head = temp

        if self.head.next is None:
            self.tail = self.head

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def search(self, node_data):
        current = self.head
        while current is not None:
            if node_data == current.data:
                return True
            current = current.next
        return False

    def remove(self, node_data):
        current = self.head
        prev = None  # defined to resolve reference
        count = 0
        is_removed = False
        while current is not None and is_removed is False:
            if current.data == node_data:
                if count == 0:
                    self.head = current.next
                    is_removed = True
                else:
                    prev.next = current.next
                    is_removed = True
            count += 1
            prev = current
            current = current.next

        if current is None:
            raise ValueError('Element not in list')

    def append(self, node_data):  # converts node data to node, iterates until it reaches the end, set .next to new node
        new_node = Node(node_data)
        current = self.head

        if current is None:
            self.head = new_node
            return

        while current.next is not None:
            current = current.next

        current.next = new_node

    def improved_append(self, node_data):  # O(1) time complexity
        new_node = Node(node_data)
        first_elem = self.head

        if first_elem is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def index(self, item):  # with accumulator, traverse list, if item == node.data, return count, otherwise raise error
        index = 0
        current = self.head

        if self.is_empty():  # account for empty list
            raise ValueError('List is empty')

        while current is not None:  #
            if current.data == item:
                return index
            current = current.next
            index += 1

        raise ValueError('Element not in list')

    def pop(self, index=None):  # takes in index and iterates until index is reached, then sets prev.next to current.nex
        count = 0
        prev = None
        current = self.head

        if self.is_empty():  # account for empty list
            raise ValueError('List is empty')

        while count is not index:
            if index is None and current.next is None:
                prev.next = None
                return current.data

            if type(index) == int and current.next is None:
                raise ValueError('Index out of range')

            current = current.next
            prev = current
            count += 1

        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next

        return current.data

    def new_pop(self, index=None):
        prev = None
        current = self.head
        count = 0


        while current is not None:
            if current.next is None and index is None:
                prev.next = current.next
                return

            if index == count:
                break

            prev = current
            current = current.next
            count += 1

        prev.next = current.next

    def insert(self, index, node_data):  #iterates until index-1 is reached, sets new_node.next = current.next, then current.next = new_node
        new_node = Node(node_data)
        count = 0
        current = self.head

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        while current is not None:
            if count == index - 1:
                break

            current = current.next
            count += 1

        if current is None:
            raise ValueError('Index out of range')
        new_node.next = current.next
        current.next = new_node

    def improved_remove(self, item):  # removes unnecessary variable 'count', breaks code into obvious steps
        current = self.head
        prev = None

        while current is not None:
            if current.data == item:
                break
            else:
                prev = current
                current = current.next

        if current is None:
            raise ValueError('Element not in list')
        elif prev is None:
            self.head = None
        else:
            prev.next = current.next


class OrderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            elif current.data > item or current.next is None:
                return False
            current = current.next

    def add(self, node_data):  #case 1: add to empty list, case 2: add to non-empty list
        new_node = Node(node_data)
        current = self.head
        prev = None

        if self.is_empty():
            self.head = new_node
            return

        while current is not None:
            if current.next is None:
                current.next = new_node
                return

            elif new_node.data <= current.data:
                new_node.next = self.head
                self.head = new_node
                return

            elif current.data <= new_node.data < current.next.data:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def model_add(self, item):
        current = self.head
        previous = None
        temp = Node(item)

        while current is not None and current.data < item:
            previous = current
            current = current.next

        if previous is None:
            temp.next = self.head
            self.head = temp
        else:
            temp.next = current
            previous.next = temp

    def improved_remove(self, item):  # removes unnecessary variable 'count', breaks code into obvious steps
            current = self.head
            prev = None

            while current is not None:
                if current.data == item:
                    break
                else:
                    prev = current
                    current = current.next

            if current is None:
                raise ValueError('Element not in list')
            elif prev is None:
                self.head = current.next
            else:
                prev.next = current.next

my_list = OrderedList()
my_list.add(32)
my_list.add(77)
my_list.add(17)
my_list.add(26)
my_list.add(54)
print(my_list.size())
print(my_list.search(54))
print(my_list.size())
