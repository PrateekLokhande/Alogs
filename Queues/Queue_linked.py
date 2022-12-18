class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        cursor = self.head
        while cursor:
            yield cursor
            cursor = cursor.next

class Queue:
    def __init__(self) -> None:
        self.LinkedList = LinkedList()

    def __str__(self) -> str:
        return "-->".join([str(x.value) for x in self.LinkedList])

    @property
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def enqueue(self, value):
        newNode = Node(value)
        if self.LinkedList.head == None:
            self.LinkedList.head = newNode
            self.LinkedList.tail = newNode
        else:
            self.LinkedList.tail.next = newNode
            self.LinkedList.tail = newNode
            
        return f"The {value} is inserted into the Que"

    @property
    def dequeue(self):
        if self.isEmpty:
            return "Que is empty"
        else:
            value = self.LinkedList.head.value  # if store value from here it also work
            if self.LinkedList.head == self.LinkedList.tail:
                self.LinkedList.head = None
                self.LinkedList.tail = None
            else:
                self.LinkedList.head = self.LinkedList.head.next
        return value

if __name__ == "__main__":
    CustumQueue = Queue()
    print(CustumQueue.enqueue(5))
    print(CustumQueue.enqueue(4))
    print(CustumQueue.enqueue(3))
    print(CustumQueue)
    print(CustumQueue.dequeue)
    print(CustumQueue)
