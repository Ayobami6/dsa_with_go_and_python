#!/usr/bin/python3
from typing import List, Any

"""Queue Operations
- Create Queue
- Enqueue
- Dequeue
- Peek
- isEmpty
- isFull
- deleteQueue
"""


# queue class

class Queue:
    """Queue object with no size limit
    """

    def __init__(self) -> None:
        self.data: list = []

    # str method
    def __str__(self) -> str:
        values: List[str] = [str(x) for x in self.data]
        return " ".join(values)

    # check if queue is empty
    def is_empty(self) -> bool:
        if self.data == []:
            return True
        return False

    # enqueu data to the queue
    def enqueue(self, data: Any) -> None:
        """Add data to the queue

        Args:
            data (any): data to be added to rhe queue
        """
        self.data.append(data)

    # dequeue data from the queue

    def dequeue(self) -> Any:
        """Remove the first entry of the queue

        Returns:
            any:  the first entry of the queue
        """
        if self.is_empty():
            raise Exception("Oops!!, Queue is empty")
        first = self.data[0]
        self.data = self.data[1:]
        return first

    def peek(self) -> Any:
        """Just returns the first item of the queue

        Returns:
            Any: The first item of the queue
        """
        if self.is_empty():
            raise Exception("Oops!!, Queue is empty")
        return self.data[0]

    def delete_queue(self) -> None:
        """The queue
        """
        self.data = []


class SizedQueue:
    def __init__(self, max_size):
        self.data = max_size * [None]
        self.max_size = max_size
        self.top = -1
        self.start = -1

    # str method
    def __str__(self) -> str:
        values: List[str] = [str(x) for x in self.data]
        return " ".join(values)

    def is_full(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.max_size:
            return True
        else:
            return False

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def enqueue(self, val) -> None:
        if self.is_empty():
            raise Exception("Oops!! Queue is empty")
        else:
            # check if the top is a the end of the queue
            if self.top + 1 == self.max_size:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.data[self.top] = val

    def dequeue(self) -> Any:
        if self.is_empty():
            raise Exception("Oops!!, Queue is empty")
        else:
            first_data = self.data[self.start]
            start = self.start
            # if the size is one, after dequeue make the queue empty
            if self.start == self.top:
                self.start = -1
                self.top = -1
            # if start pointer is at the end of the queue, reset the start to first data point
            elif self.start + 1 == self.max_size:
                self.start = 0
            else:
                self.start += 1
            self.data[start] = None
            return first_data

    def peek(self) -> Any:
        if self.is_empty():
            raise Exception("Oops!!, Queue is empty")
        return self.data[self.start]


new_queue = Queue()

new_queue.enqueue(2)
new_queue.enqueue(3)
new_queue.enqueue(4)
print(new_queue.peek())
data = new_queue.dequeue()
print(f"This is the dequeued data {data}")
print(new_queue)
