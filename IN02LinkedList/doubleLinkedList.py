class Node:
    def __init__(self, data,  prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

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
            print("List is Empty")
            return True
        else:
            return False

    # 특정 노드 선택
    def selectNodeWithIndex(self, index):
        if self.isEmpty():
            return None
        elif index >= self.size:
            print("Index over range")
            return None
        if index == 0:
            return self.head
        elif index > self.size // 2:
            targetNode = self.head
            for _ in range(self.getListSize-1, index, -1):
                targetNode = targetNode.prev
            return targetNode
        else:
            for _ in range(index):
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

    def appendHead(self, value):
        if self.isEmpty():
            self.head = Node(value)
            self.tail = self.head
        else:
            newNode = Node(value, next=self.head)
            self.head.prev = newNode
            self.head = newNode
        self.size += 1

    # 테일 노드 추가
    def append(self, value):
        if self.isEmpty():
            self.head = Node(value)
            self.tail = self.head
        else:
            newNode = Node(value, self.tail)
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1

    # 삽입
    def insert(self, value, index):
        if index >= self.size:
            print("Index over range")
            return
        if self.isEmpty():
            self.head = Node(value)
            self.tail = self.head
        elif index == 0:
            newNode = Node(value, None, self.head)
            self.head.prev = newNode
            self.head = newNode
        else:
            node = self.selectNodeWithIndex(index)
            newNode = Node(value, node.prev, node)
            node.prev.next = newNode
            node.prev = newNode
        self.size += 1

    # 노드 삭제
    def deleteWithIndex(self, index):
        if self.isEmpty():
            return
        if index >= self.size:
            print("Index over range")
            return
        elif index == 0:
            targetNode = self.head
            if(self.size == 1):
                del(targetNode)
                self.head = self.tail = None
            else:
                self.head = targetNode.next
                self.head.prev = None
                del(targetNode)
        else:
            prevNode = self.selectNodeWithIndex(index-1)
            targetNode = prevNode.next
            prevNode.next = targetNode.next
            if(targetNode == self.tail):
                self.tail = prevNode
            elif(targetNode.next != None):
                targetNode.next.prev = prevNode
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
            prevNode = self.tail.prev
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
                print("[{0}]<->".format(node.data), end="")
                node = node.next
            else:
                print("[{0}]".format(node.data))
                break


if __name__ == "__main__":
    dList = DoubleLinkedList()
    dList.append(1)
    dList.append(2)
    dList.append(3)
    dList.printList()

    dList.insert(4, 1)
    dList.printList()
    dList.deleteWithIndex(2)
    dList.printList()
    print("--------------------------------")
    print(dList.selectNodeWithIndex(3))
    print(dList.selectNodeWithIndex(0).data)
    print(dList.selectNodeWithValue(5))
    print(dList.selectNodeWithValue(1).data)

    lList = dList.getAll()
    print("lList: ", lList)

    dList.printList()
    print("head: ", dList.head.data)
    print("tail: ", dList.tail.data)
    print("tail's prev: ", dList.tail.prev.data)

    dList.delete()
    dList.printList()

    dList.delete()
    dList.printList()
    dList.delete()
    dList.printList()

    print("==================================")
    dList.delete()
    dList.printList()

    dList.selectNodeWithIndex(1)
    dList.deleteWithIndex(1)
