class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self, top=None, capacity=None):
        self.top = top
        self.size = 0
        self.capacity = capacity

    def pop(self):
        if(self.isEmpty()):
            print("Stack is empty.")
            return None
        item = self.top
        self.top = self.top.next
        self.size -= 1
        return item

    def push(self, item):
        if(self.isFull()):
            print("Stack is full.")
            return
        node = Node(item)
        if(self.size == 0):
            self.top = node
            self.top.next = None
        else:
            node.next = self.top
            self.top = node
        self.size += 1

    def pushNode(self, item:Node):
        if(self.isFull()):
            print("Stack is full.")
            return
        if(self.size == 0):
            self.top = item
            self.top.next = None
        else:
            item.next = self.top
            self.top = item
        self.size += 1

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        item = self.top
        return item

    def isEmpty(self):
        if (self.size <= 0):
            return True
        else:
            return False

    def isFull(self):
        if(self.capacity == None):
            return False
        elif(self.size >= self.capacity):
            return True
        else:
            return False

    def printStack(self):
        node = self.top
        while(node != None):
            print("{0}]".format(node.data), end="")
            node = node.next
        print("")


if __name__ == "__main__":
    myStack = Stack(capacity=3)
    myStack.push(1)
    myStack.push(2)
    myStack.push(3)
    myStack.push(4)
    myStack.printStack()
    print("--------------------------------")
    print("Pop: ", myStack.pop().data)
    myStack.printStack()
    print("Peek: ", myStack.peek().data)
    myStack.printStack()
    myStack.pop()
    myStack.pop()
    print("--------------------------------")
    myStack.pop()
    myStack.pop()
