## 한 개로 세개 ##

from Stack import *
import copy

# 배열에 node class를 저장
# node stack number가 있음
# 각 stack number의 top을 유지시키는 방법을 사용


class triNode(Node):
    def __init__(self, stackNo, data, nextNode=None):
        self.stackNo = stackNo
        Node.__init__(self, data, nextNode)


class MultiStack:
    def __init__(self, top1=None, top2=None, top3=None):
        self.multiStack = []
        self.top1 = top1
        self.top2 = top2
        self.top3 = top3

    def push(self, node):
        if(node.stackNo == 1):
            node.next = self.top1
            self.top1 = node
        elif(node.stackNo == 2):
            node.next = self.top2
            self.top2 = node
        elif(node.stackNo == 3):
            node.next = self.top3
            self.top3 = node
        self.multiStack.append(node)

    def pop(self, no):
        if(no == 1):
            if(self.top1 == None):
                return
            item = copy.copy(self.top1)
            temp = self.top1
            self.top1 = self.top1.next
            self.multiStack.remove(temp)
            return item
        elif(no == 2):
            if(self.top2 == None):
                return
            item = copy.copy(self.top2)
            temp = self.top2
            self.top2 = self.top2.next
            self.multiStack.remove(temp)
            return item
        elif(no == 3):
            if(self.top3 == None):
                return
            item = copy.copy(self.top3)
            temp = self.top3
            self.top3 = self.top3.next
            self.multiStack.remove(temp)
            return item

    def peek(self, no):
        if(no == 1):
            if(self.top1 == None):
                return
            item = copy.copy(self.top1)
            return item
        elif(no == 2):
            if(self.top2 == None):
                return
            item = copy.copy(self.top2)
            return item
        elif(no == 3):
            if(self.top3 == None):
                return
            item = copy.copy(self.top3)
            return item


def Solution1():
    mStack = MultiStack()
    mStack.push(triNode(data="1-1", stackNo=1))
    mStack.push(triNode(data="2-1", stackNo=2))
    mStack.push(triNode(data="3-1", stackNo=3))
    mStack.push(triNode(data="1-2", stackNo=1))
    mStack.push(triNode(data="1-3", stackNo=1))
    mStack.push(triNode(data="2-2", stackNo=2))
    mStack.push(triNode(data="3-2", stackNo=3))
    mStack.push(triNode(data="2-3", stackNo=2))
    mStack.push(triNode(data="3-3", stackNo=3))
    mStack.push(triNode(data="3-4", stackNo=3))

    for i in mStack.multiStack:
        print(i.data)
    print("++++++++++++++++++++++++++++++")
    print("POP: ", mStack.pop(1).data)
    for i in mStack.multiStack:
        print(i.data)
    print("++++++++++++++++++++++++++++++")
    print("POP: ", mStack.pop(2).data)
    for i in mStack.multiStack:
        print(i.data)
    print("++++++++++++++++++++++++++++++")
    print("POP: ", mStack.pop(3).data)
    print("POP: ", mStack.pop(3).data)
    for i in mStack.multiStack:
        print(i.data)
    
if __name__ == "__main__":
    Solution1()
