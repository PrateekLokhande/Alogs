class Queue:
    def __init__(self, maxSize) -> None:
        self.maxSize = maxSize
        self.item = maxSize * [None]
        self.start = -1
        self.top = -1

    @property
    def isFull(self):
        if self.top + 1 == self.start:
            print(f"start at {self.start}, Top at {self.top + 1}")
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            print(f"start at {self.start}, Top at {self.top + 1}")
            return True
        else:
            return False

    @property
    def isEmpty(self):
        if self.start == -1 and self.top == -1:
            return True
        else:
            return False

    def __str__(self) -> str:
        print(f"start at {self.start}, Top at {self.top}")
        return "-->".join([str(i) for i in self.item])

    def enqueue(self, value):
        if self.isFull:
            return "Queue is Full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top +=1
                if self.start == -1:
                    self.start = 0

            self.item[self.top] = value
            return f"The {value} is inserted into the Que at {self.top}"
    
    @property
    def dequeue(self):
        if self.isEmpty:
            return "Nothing to remove , queue is empty"
        else:
            firstElement = self.item[self.start]
            start = self.start

            if self.start == self.top:
                self.top = self.start = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.item[start] = None
            return firstElement
            


CustumQueue = Queue(5)
print(CustumQueue.isFull)
print(CustumQueue.isEmpty)

print(CustumQueue.enqueue(5))
print(CustumQueue.enqueue(4))
print(CustumQueue.enqueue(3))
print(CustumQueue)
print(CustumQueue.enqueue(2))
print(CustumQueue.enqueue(1))
print(CustumQueue)
print(CustumQueue.dequeue)
print(CustumQueue.dequeue)
print(CustumQueue.enqueue(1))
print(CustumQueue.enqueue(6))
print(CustumQueue.enqueue(7))
print(CustumQueue.dequeue)
print(CustumQueue)