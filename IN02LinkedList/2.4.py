## 분할 ##

from singleLinkedList import SingleLinkedList as LinkedList
import copy

sList = LinkedList()
sList.append(3)
sList.append(5)
sList.append(8)
sList.append(5)
sList.append(10)
sList.append(2)
sList.append(1)

# 두 개의 리스트로 분리 후 합친다.
# 추가 연결리스트 필요.
# BCR O(N)
# 원소의 stable을 보장한다 -> 원소의 순서를 보장
def Solution1():
    x = int(input("x: "))

    def pertition(head, value):
        leftHead = None
        leftTail = None
        rightHead = None
        rightTail = None
        while(head != None):
            # 연결을 끊어주고 연결해야함..!
            node = copy.copy(head)
            node.next = None
            if(node.data < value):
                if(leftHead != None):
                    leftTail.next = node
                    leftTail = leftTail.next
                else:
                    leftHead = node
                    leftTail = node
                # print(leftHead.data)
            else:
                if(rightHead != None):
                    rightTail.next = node
                    rightTail = rightTail.next
                else:
                    rightHead = node
                    rightTail = rightHead
            head = head.next

        if(leftHead == None):
            return rightHead, rightTail
        else:
            leftTail.next = rightHead
            return leftHead, rightTail

    head, tail = pertition(sList.head, x)
    resultList = LinkedList(head=head, tail=tail)
    resultList.calculateListSize()
    sList.printList()
    resultList.printList()


# 원소의 stable을 보장하지 않아도 되는 경우.
# 일부 변수를 줄일 수 있다.
# 내 해답과 같은 맥락 prev, next 
# 해당 리스트 내에서 원소의 순서를 변경
def Solution2():
    x = int(input("x: "))

    def partition(node, x):
        head = tail = node
        while(node != None):
            nextNode = node.next
            if(node.data < x):
                node.next = head
                head = node
            else:
                tail.next = node
                tail = node
            node = nextNode
        tail.next = None
        return head

    sList.head = partition(sList.head, x)
    sList.printList()

if __name__ == "__main__":
    #Solution1()
    Solution2()
