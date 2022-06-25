## 스택으로 큐 ##

from Stack import *

# pop역할을 하는 스택이 빌 때 마다 push stack을 뒤집어 준다.
def Solution1():
    class MyQueue:
        def __init__(self):
            self.pushStack = Stack()
            self.popStack = Stack()
            self.size = 0

        def add(self, data):
            self.pushStack.push(data)
            self.size += 1

        def remove(self):
            if(self.isEmpty()):
                print("Queue is Empty.")
                return
            if(self.popStack.isEmpty()):
                self.reverse()
            self.size -= 1
            return self.popStack.pop()

        def isEmpty(self):
            if(self.pushStack.isEmpty() and self.popStack.isEmpty()):
                return True
            else:
                return False

        def reverse(self):
            while(not self.pushStack.isEmpty()):
                node = self.pushStack.pop()
                self.popStack.push(node.data)

        def printAll(self):
            counter = self.size
            pops = self.popStack.top
            pushs = self.pushStack.top
            print("C: " , counter)

            def printPushStack(head, counter):
                if(head == None or counter <= 0):
                    return
                nextNode = head.next
                counter -= 1
                printPushStack(nextNode, counter)
                print("{0}]".format(head.data), end="")

            while(pops != None):
                print("{0}]".format(pops.data), end="")
                pops = pops.next
                counter -= 1
            printPushStack(pushs, self.size)
            print("")

    q = MyQueue()
    q.add(1)
    q.add(2)
    q.add(3)
    q.add(4)
    q.add(5)
    q.printAll()
    print("+++++++++++++++++++++")
    q.remove()
    q.printAll()
    print("+++++++++++++++++++++")
    q.add(6)
    q.add(7) 
    q.printAll()

if __name__ == "__main__":
    Solution1()
