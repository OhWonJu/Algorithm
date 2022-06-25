from Stack import *

## 접시 무더기 ##      ## 솔루션2 미해결..

# 시간복잡도를 우선시 하는 경우.
# 중간 중간 비어 있는 stack을 인정하는 경우이다.
def Solution1():
    class SetOfStack:
        def __init__(self, capacity=None):
            self.capacity = capacity
            self.stacks = []
            self.index = 0

        def push(self, item):
            if(len(self.stacks) == 0):
                self.stacks.append(Stack(capacity=self.capacity))
                self.stacks[self.index].push(item)
            elif(self.stacks[self.index].isFull()):
                print("Recent stack is Full!")
                self.stacks.append(Stack(capacity=self.capacity))
                self.index += 1
                self.stacks[self.index].push(item)
            else:
                self.stacks[self.index].push(item)
            pass

        def pop(self):
            if(self.stacks[self.index].isEmpty()):
                print("Recent Stack is Empty!")
                target = self.stacks[self.index]
                self.stacks.remove(target)
                self.index -= 1
                if(self.index < 0):
                    print("Set of Stack is empty.")
                    return
                return self.stacks[self.index].pop()
            else:
                self.stacks[self.index].pop()

        def popAt(self, index):
            if(index < 0 or index > self.index):
                print("Index over range")
                return None
            else:
                if(self.stacks[index].size == 1):
                    value = self.stacks[index].pop()
                    self.stacks.remove(self.stacks[index])
                    self.index -= 1
                    return value
                return self.stacks[index].pop()

        def printAll(self):
            for i in range(self.index+1):
                self.stacks[i].printStack()

    sStack = SetOfStack(capacity=3)
    sStack.push(1)
    sStack.push(2)
    sStack.push(3)
    sStack.push(4)
    sStack.push(5)
    sStack.push(6)
    sStack.push(7)
    sStack.push(8)

    sStack.printAll()
    print("++++++++++++++++++++++++++")

    sStack.pop()
    sStack.pop()
    sStack.printAll()
    print("++++++++++++++++++++++++++")

    sStack.pop()
    sStack.printAll()

    print("++++++++++++++++++++++++++")
    sStack.push(6)
    sStack.push(7)
    sStack.push(8)
    sStack.printAll()
    print("++++++++++++++++++++++++++")

    sStack.popAt(1)
    sStack.printAll()
    print("++++++++++++++++++++++++++")

    sStack.popAt(1)
    sStack.popAt(1)
    sStack.printAll()
    print("++++++++++++++++++++++++++")

    sStack.popAt(1)
    sStack.popAt(1)
    sStack.printAll()
    print("++++++++++++++++++++++++++")

    sStack.pop()
    sStack.pop()
    sStack.printAll()
    print("++++++++++++++++++++++++++")
    sStack.pop()
    sStack.pop()

# 공간 복잡도를 우선시 하는 경우.
# 마지막 스택을 제외하고는 모두 채워져 있는 상태이다.


def Solution2():
    class Node:
        def __init__(self, data, above=None, below=None):
            self.data = data
            self.above = above
            self.below = below

    class Stack:
        def __init__(self, capacity=None, top=None, bottom=None):
            self.top = top
            self.bottom = bottom
            self.capacity = capacity
            self.size = 0

        def join(self, above: Node, below: Node):
            if(below != None):
                below.above = above
            if(above != None):
                above.below = below

        def pop(self):
            if(self.isEmpty()):
                print("Stack is empty.")
                return None
            item = self.top
            self.top = self.top.below
            self.size -= 1
            return item

        def push(self, item):
            if(self.isFull()):
                print("Stack is full.")
                return
            item = Node(item)
            if(self.size == 0):
                self.bottom = item
            self.join(item, self.top)
            self.top = item
            self.size += 1

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

        def removeBottom(self):
            b = self.bottom
            self.bottom = self.bottom.above
            if(self.bottom != None):
                self.bottom.below = None
            self.size -= 1
            return b

        def printStack(self):
            node = self.top
            while(node != None):
                print("{0}]".format(node.data), end="")
                node = node.below
            print("")

    class SetOfStack:
        def __init__(self, capacity=None):
            self.capacity = capacity
            self.stacks = []
            self.index = 0

        def push(self, item):
            if(len(self.stacks) == 0):
                self.stacks.append(Stack(capacity=self.capacity))
                self.stacks[self.index].push(item)
            elif(self.stacks[self.index].isFull()):
                print("Recent stack is Full!")
                self.stacks.append(Stack(capacity=self.capacity))
                self.index += 1
                self.stacks[self.index].push(item)
            else:
                self.stacks[self.index].push(item)
            pass

        def pop(self):
            if(self.stacks[self.index].isEmpty()):
                print("Recent Stack is Empty!")
                target = self.stacks[self.index]
                self.stacks.remove(target)
                self.index -= 1
                if(self.index < 0):
                    print("Set of Stack is empty.")
                    return
                return self.stacks[self.index].pop()
            else:
                self.stacks[self.index].pop()

        def popAt(self, index):
            return self.leftShift(index, True)

        # recursion을 사용해서 바닥 원소 밀어내기
        def leftShift(self, index, removeTop):
            stack = self.stacks[index]
            removeItem = None
            if(removeTop):
                removeItem = stack.pop()
            else:
                removeItem = stack.removeBottom()
            if(stack.isEmpty()):
                self.stacks.remove(stack)
            elif self.index > index+1:
                v = self.leftShift(index+1, False)
                stack.push(v)
            return removeItem

        def printAll(self):
            for stack in self.stacks:
                stack.printStack()

    sStack = SetOfStack(capacity=3)
    sStack.push(1)
    sStack.push(2)
    sStack.push(3)
    sStack.push(4)
    sStack.push(5)
    sStack.push(6)
    sStack.push(7)
    sStack.push(8)

    sStack.printAll()
    print("++++++++++++++++++++++++++")

    sStack.pop()
    sStack.pop()
    sStack.printAll()
    print("++++++++++++++++++++++++++")

    sStack.pop()
    sStack.printAll()

    print("++++++++++++++++++++++++++")
    sStack.push(6)
    sStack.push(7)
    sStack.push(8)
    sStack.printAll()
    print("++++++++++++++++++++++++++")

    sStack.popAt(1)
    sStack.printAll()
    print("++++++++++++++++++++++++++")

    sStack.popAt(1)
    sStack.popAt(1)
    sStack.printAll()
    print("++++++++++++++aa++++++++++++")

    sStack.popAt(1)
    sStack.popAt(1)
    sStack.printAll()
    print("++++++++++++asd+++++++++++++")

    sStack.pop()
    sStack.pop()
    sStack.printAll()
    print("++++++++++++++++++++++++++")
    sStack.pop()


if __name__ == "__main__":
    # Solution1()
    Solution2()
