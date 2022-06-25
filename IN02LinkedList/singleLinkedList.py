class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SingleLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.size = 0

    def calculateListSize(self):
        self.size = 0
        node = self.head
        while(node != None):
            self.size += 1
            node = node.next

    # 리스트 사이즈
    def getListSize(self):
        return self.size

    def getAll(self):
        result = []
        node = self.head
        while node:
            result.append(node.data)
            node = node.next
        return result

    # 리스트 empty 여부
    def isEmpty(self):
        if(self.size == 0):
            return True
        else:
            return False

    # 특정 노드 선택
    def selectNodeWithIndex(self, index):
        if self.isEmpty():
            print("List is Empty")
            return None
        if(index >= self.size):
            print("Index over range")
            return None
        if index == 0:
            return self.head
        else:
            targetNode = self.head
            for _ in range(index):
                targetNode = targetNode.next
            return targetNode

    def selectNodeWithValue(self, value):
        targetNode = self.head
        for _ in range(self.size):
            if(targetNode.data == value):
                return targetNode
            else:
                targetNode = targetNode.next
        print("Value is not in Linked List")

    # 테일 노드 추가
    def append(self, value):
        if self.isEmpty():
            self.head = Node(value)
            self.tail = self.head
            self.size += 1
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
            self.size += 1

    # 삽입
    def insert(self, value, index):
        if self.isEmpty():
            self.head = Node(value)
            self.tail = self.head
            self.size += 1
        elif index == 0:
            self.head = Node(value, self.head)
            self.size += 1
        else:
            prevNode = self.selectNodeWithIndex(index-1)
            if(prevNode == None):
                return
            newNode = Node(value)
            newNode.next = prevNode.next
            prevNode.next = newNode
            self.size += 1

    def connectLists(self, target, head=None):
        self.tail.next = target.head
        self.tail.next = target.head if head == None else head
        self.tail = target.tail
        self.calculateListSize()

    # 노드 삭제
    def deleteWithIndex(self, index):
        if self.isEmpty():
            print("List is Empty")
            return
        elif index >= self.size:
            print("Index over range")
            return
        elif index == 0:
            targetNode = self.head
            if(self.size == 1):
                del(targetNode)
                self.head = self.tail = None
            else:
                self.head = targetNode.next
                del(targetNode)
                self.size -= 1
        else:
            prevNode = self.selectNodeWithIndex(index-1)
            targetNode = prevNode.next
            prevNode.next = targetNode.next
            if(targetNode == self.tail):
                self.tail = prevNode
            del(targetNode)
            self.size -= 1

    def delete(self):
        if self.isEmpty():
            print("List is Empty")
            return
        elif self.size == 1:
            del(self.head)
            self.head = self.tail = None
        else:
            prevNode = self.selectNodeWithIndex(self.size-2)
            targetNode = self.tail
            self.tail = prevNode
            prevNode.next = None
            del(targetNode)
        self.size -= 1

    # 리스트 출력
    def printList(self):
        node = self.head
        print("ListSize: {}".format(self.getListSize()))
        while(node):
            if(node.next != None):
                print("[{0}]->".format(node.data), end="")
                node = node.next
            else:
                print("[{0}]".format(node.data))
                break


if __name__ == "__main__":
    sList = SingleLinkedList()
    sList.append(1)
    sList.append(2)
    sList.append(3)
    sList.printList()

    sList.insert(4, 1)
    sList.printList()
    sList.deleteWithIndex(3)
    sList.printList()
    print("--------------------------------")
    print(sList.selectNodeWithIndex(3))
    print(sList.selectNodeWithIndex(0).data)
    print(sList.selectNodeWithValue(5))
    print(sList.selectNodeWithValue(1))
    print("--------------------------------")
    lList = sList.getAll()
    print("lList: ", lList)

    sList.printList()
    print("head: ", sList.head.data)
    print("tail: ", sList.tail.data)

    sList.delete()
    sList.printList()

    sList.delete()
    sList.printList()
    sList.delete()
    sList.printList()

    print("==================================")
    sList.delete()
    sList.printList()

    sList.selectNodeWithIndex(1)
    sList.deleteWithIndex(1)
