'''
Queue abstract data type
Methods: enqueue, dequeue, is empty, size,
'''
from random import randrange
from c4_BasicDataStructures.chapter4_stack import Stack


class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
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


class AltQueue:
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.pop(0)

    def is_empty(self):
        return not bool(self._items)

    def size(self):
        return len(self._items)

    def peek_front(self):
        return self._items[0]

    def peek_rear(self):
        return self._items[-1]

    def __str__(self):
        return str(self._items)


class StackQueue:
    """creates a queue ADT where amortized time complexity of enqueue and dequeue is O(1)"""
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enQueue(self, item):
        self.stack1.push(item)

    def deQueue(self):
        s1 = self.stack1
        s2 = self.stack2
        if s1.is_empty() and s2.is_empty():
            raise IndexError('Dequeueing from empty queue')
        elif s2.is_empty() and not s1.is_empty():
            while not s1.is_empty():
                s2.push(s1.pop())
        return s2.pop()

    def size(self):
        return self.stack1.size() + self.stack2.size()

    def is_empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()


q = StackQueue()
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)

print(q.deQueue())
print(q.deQueue())
print(q.deQueue())

def hot_potato(name_list, count):
    q = Queue()
    for name in name_list:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(count):
            q.enqueue(q.dequeue())
        q.dequeue()

    return q.dequeue()


def printer_queue_simulator(duration, print_rate):
    """returns the average wait time per task in seconds"""
    printer_queue = Queue()

    task_received = 0
    waiting_time = 0

    for current_time in range(duration): #iterates through every second to check for tasks
        is_printer_busy = not printer_queue.is_empty()
        rng = randrange(1, 181)
        if rng == 180:
            """if task received, calculate when task is done and queue it"""
            task_received += 1
            pages_to_print = randrange(1, 21)
            time_to_complete = int(pages_to_print/(print_rate/60))
            if is_printer_busy:
                """completed timestamp of received task depends on next task"""
                last_in_queue = printer_queue.peek_rear()
                timestamp_completed = last_in_queue + time_to_complete
            else:
                timestamp_completed = current_time + time_to_complete
            printer_queue.enqueue(timestamp_completed)
            waiting_time += timestamp_completed - current_time

        if is_printer_busy:
            first_in_queue = printer_queue.peek_front()
            if current_time == first_in_queue:
                printer_queue.dequeue()

    average_wait_time = waiting_time/task_received
    return f'Average wait time {average_wait_time:.2f} Tasks remaining {printer_queue.size()}'

for i in range(10):
    print(printer_queue_simulator(3600, 40))

