## 스택 정렬 ##

from Stack import *


# 만약에 사용할 수 있는 스택의 수에 제한이 없다면?
# merge sort를 구현 가능
def Solution1():
    class SortedStack:
        def __init__(self, capacity=None, main=int(False)):
            self.main = main
            self.capacity = capacity
            self.stacks = (Stack(), Stack())

        def push(self, data):
            self.stacks[self.main].push(data)

        def pushWithSort(self, data):
            if(self.stacks[self.main].isEmpty()):
                self.stacks[self.main].push(data)
                return
            while(not self.stacks[self.main].isEmpty() and self.stacks[self.main].top.data < data):
                self.stacks[int(not self.main)].push(
                    self.stacks[self.main].pop().data)
            self.stacks[self.main].push(data)
            while(not self.stacks[int(not self.main)].isEmpty()):
                self.stacks[int(self.main)].push(
                    self.stacks[not self.main].pop().data)

        def pop(self):
            return self.stacks[self.main].pop()

        def peek(self):
            return self.stacks[self.main].peek()

        def sort(self, size):
            if(size <= 0):
                return
            maxNode = self.stacks[self.main].pop()
            counter = 0
            while(counter < size-1):
                if(maxNode.data < self.stacks[self.main].top.data):
                    self.stacks[not self.main].pushNode(maxNode)
                    maxNode = self.stacks[self.main].pop()
                else:
                    self.stacks[not self.main].pushNode(
                        self.stacks[self.main].pop())
                counter += 1
            self.stacks[self.main].pushNode(maxNode)
            while(not self.stacks[not self.main].isEmpty()):
                self.stacks[self.main].pushNode(
                    self.stacks[not self.main].pop())
            self.stacks[self.main].printStack()
            size -= 1
            self.sort(size)

        def printAll(self):
            self.stacks[self.main].printStack()

    myStack = SortedStack()
    myStack.push(1)
    myStack.push(4)
    myStack.push(6)
    myStack.push(7)
    myStack.push(8)
    myStack.push(5)
    myStack.printAll()
    print("==========================")
    myStack.sort(size=myStack.stacks[myStack.main].size)
    myStack.printAll()
    print("++++++++++++++++++++++++++")
    myStack.pushWithSort(2)
    myStack.pushWithSort(3)
    myStack.printAll()


# Solution1의 pushWithSort 개념을 확장.
# Sort 자체를 pushWithSort 처럼 한다면...일반 push로 인한 비정렬 상태에서의 정렬을 좀 더 효율적으로 ?
def Solution2():
    class SortedStack:
        def __init__(self, capacity=None, main=int(False)):
            self.main = main
            self.capacity = capacity
            self.stacks = (Stack(), Stack())

        def push(self, data):
            self.stacks[self.main].push(data)

        def pushWithSort(self, data):
            if(self.stacks[self.main].isEmpty()):
                self.stacks[self.main].push(data)
                return
            while(not self.stacks[self.main].isEmpty() and self.stacks[self.main].top.data < data):
                self.stacks[int(not self.main)].push(
                    self.stacks[self.main].pop().data)
            self.stacks[self.main].push(data)
            while(not self.stacks[int(not self.main)].isEmpty()):
                self.stacks[int(self.main)].push(
                    self.stacks[not self.main].pop().data)

        def pop(self):
            return self.stacks[self.main].pop()

        def peek(self):
            return self.stacks[self.main].peek()

        def sort(self):
            # 원소의 크기가 작은 순으로 sub stack에 저장 
            while(not self.stacks[self.main].isEmpty()):
                temp = self.stacks[self.main].pop()
                while(not self.stacks[not self.main].isEmpty() and self.stacks[not self.main].peek().data > temp.data):
                    self.stacks[self.main].pushNode(
                        self.stacks[not self.main].pop())
                self.stacks[not self.main].pushNode(temp)
            # 작은 순으로 정렬이 완료되면, stack을 뒤집기
            while(not self.stacks[not self.main].isEmpty()):
                self.stacks[self.main].pushNode(
                    self.stacks[not self.main].pop())

        def printAll(self):
            self.stacks[self.main].printStack()

    myStack = SortedStack()
    myStack.push(1)
    myStack.push(4)
    myStack.push(6)
    myStack.push(7)
    myStack.push(8)
    myStack.push(5)
    myStack.printAll()
    print("==========================")
    myStack.sort()
    myStack.printAll()
    print("++++++++++++++++++++++++++")
    myStack.pushWithSort(2)
    myStack.pushWithSort(3)
    myStack.printAll()

## 스택을 무한정 사용 가능한 경우
## merge sort
## quick sort 구현 해보기...

if __name__ == "__main__":
    #Solution1()
    Solution2()

