class Node:
    def __init__(self, data, above=None, below=None):
        self.data = data
        self.above = above
        self.below = below


class Queue:
    def __init__(self, head=None, tail=None, capacity=None):
        self.head = head
        self.tail = tail
        self.capacity = capacity
        self.size = 0

    def add(self, data):
        if(self.isFull()):
            print("Queue is Full.")
            return
        node = Node(data=data)
        if(self.isEmpty()):
            self.head = self.tail = node
        else:
            node.below = self.tail
            self.tail.above = node
            self.tail = node
        self.size += 1

    def remove(self):
        if(self.isEmpty()):
            print("Queue is Empty.")
            return
        node = None
        if(self.size == 1):
            node = self.head
            self.head = self.tail = None
        else:
            node = self.head
            self.head = self.head.above
            self.head.below = None
        self.size -= 1
        return node

    def peek(self):
        node = self.head
        return node

    def isEmpty(self):
        if(self.size == 0):
            return True
        else:
            return False

    def isFull(self):
        if(self.capacity != None and self.size >= self.capacity):
            return True
        else:
            return False

    def printQueue(self):
        node = self.head
        while(node != None):
            print("{0}]".format(node.data), end="")
            node = node.above
        print("")


if __name__ == "__main__":
    myQueue = Queue(capacity=3)
    myQueue.add(1)
    myQueue.add(2)
    myQueue.add(3)
    myQueue.add(4)
    myQueue.printQueue()
    print("--------------------------------")
    print("Pop: ", myQueue.remove().data)
    myQueue.printQueue()
    print("Peek: ", myQueue.peek().data)
    myQueue.printQueue()
    myQueue.remove()
    myQueue.remove()
    print("--------------------------------")
    myQueue.remove()
    myQueue.remove()
