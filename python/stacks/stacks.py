#!/usr/bin/python3

"""
Stack Basic implementation
- Create
- Pop 
- Push
- Peep
- isEmpty
- Size
- isFull
- deleteStack
"""

# stack with list


class StackList:
    def __init__(self, size):
        self.size = size
        self.data = []

    # check if is empty
    def is_empty(self) -> bool:
        if self.data == []:
            return True
        else:
            return False

    # push
    def push(self, val):
        if len(self.data) == self.size:
            raise Exception("Stack Overflow")
        self.data.append(val)

    def __str__(self) -> str:
        values_to_str = [str(val) for val in self.data]
        return "\n".join(values_to_str)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is Empty")

        popped = self.data.pop()
        return popped

    # to check id stack is full
    def is_full(self):
        if len(self.data) == self.size:
            return True
        else:
            return False

    def peep(self):
        if self.is_empty():
            raise Exception("Sorry, stack is empty!")
        return self.data[-1]

    def delete_stack(self):
        self.data = []


new_stack = StackList(4)

new_stack.push(3)
new_stack.push(4)
new_stack.push(4)
new_stack.push(4)
# new_stack.push(4)

# print(new_stack.is_full())
# print(new_stack.is_empty())

new_stack.delete_stack()

# popped = new_stack.pop()

peeped = new_stack.peep()

print(peeped)
# print(popped)


print(new_stack.size)
