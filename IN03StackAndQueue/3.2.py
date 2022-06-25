## 스택 Min ##

from Stack import *

# 저장되는 Node 최소값을 기록하는 방식
# 시간복잡도 O(1)을 유지하지만, 공간복잡도를 희생하게 된다.


def Solution1():
    class Node:
        def __init__(self, data, next=None, minValue=None):
            self.data = data
            self.next = next
            self.min = minValue

    class MinStack(Stack):
        def __init__(self):
            Stack.__init__(self)

        def push(self, item):
            if(self.isFull()):
                print("Stack is full.")
                return
            elif(self.size == 0):
                self.top = Node(item)
                self.top.min = self.top.data
                self.top.next = None
            else:
                item = Node(item)
                item.min = min(item.data, self.top.min)
                item.next = self.top
                self.top = item
            self.size += 1

        def min(self):
            print("Stacks min value is ", self.top.min)

    mStack = MinStack()
    mStack.push(2)
    mStack.push(3)
    mStack.push(4)
    mStack.push(1)
    mStack.push(2)
    mStack.push(3)
    mStack.push(4)

    for _ in range(7):
        mStack.min()
        mStack.pop()

# 최소값을 저장하는 stack을 하나 더 사용하는 경우
# 최악의 경우를 제외하고 공간복잡도를 줄일 수 있다.


def Solution2():
    class MinStack(Stack):
        def __init__(self):
            Stack.__init__(self)
            self.minStack = Stack()

        def push(self, item):
            if(self.isFull()):
                print("Stack is full.")
                return
            elif(self.size == 0):
                self.top = Node(item)
                self.minStack.push(item)
                self.top.next = None
            else:
                if(item <= self.minStack.peek().data):
                    self.minStack.push(item)
                item = Node(item)
                item.next = self.top
                self.top = item
            self.size += 1

        def pop(self):
            if(self.isEmpty()):
                print("Stack is empty.")
                return None
            item = self.top
            if(item.data == self.minStack.peek().data):
                self.minStack.pop()
            self.top = self.top.next
            self.size -= 1
            return item

        def min(self):
            print("Stacks min value is ", self.minStack.peek().data)

    mStack = MinStack()
    mStack.push(2)
    mStack.push(3)
    mStack.push(4)
    mStack.push(1)
    mStack.push(2)
    mStack.push(3)
    mStack.push(4)

    for _ in range(7):
        mStack.min()
        mStack.pop()


if __name__ == "__main__":
    #Solution1()
    Solution2()
