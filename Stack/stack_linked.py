class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __iter__(self):
        cursor = self.head
        while cursor:
            yield cursor
            cursor = cursor.next

class Stack:
    def __init__(self) -> None:
        self.LinkedList = LinkedList()

    def __str__(self):
        value = [str(x.value) for x in self.LinkedList]
        return "-->".join(value)

    def push(self, value):
        newNode = Node(value)
        if self.LinkedList.head == None:
            self.LinkedList.head = newNode
        else:
            newNode.next = self.LinkedList.head
            self.LinkedList.head = newNode

    def pop(self):
        if self.LinkedList.head == None:
            return "Stack is empty"
        else:
            value = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return f'poped out from stack {value}'


CustomStack = Stack()

CustomStack.push(1)
CustomStack.push(2)
CustomStack.push(3)

print(CustomStack)

print(CustomStack.pop())
print(CustomStack)
print(CustomStack.pop())
print(CustomStack.pop())
print(CustomStack.pop())