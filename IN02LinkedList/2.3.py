## 중간 노드 삭제 ##

from singleLinkedList import SingleLinkedList as LinkedList

sList = LinkedList()
sList.append(1)
sList.append(2)
sList.append(3)
sList.append(4)
sList.append(5)

# 특정 노드에만 접근 가능할 때 해당 노드를 지우고
# 연결 리스트를 유지하는 방법에 대한 문제
# targetNode를 옮겨 담고 targetNode 자리에 targetNode.next를 준다.
# 단방향의 경우 Node가 tail인 경우 완벽하게 제거할 수 없다.
# tail node가 주어졌을 경우 어떻게 처리해야 할까?
# 1. ruuner, 2. 비움 표시
def Solution1():
    targetNode = sList.selectNodeWithIndex(2)

    def deleteNode(node):
        if node.next == None:
            node.data = None
            node.next = None
            return
        if node == None:
            return

        nextNode = node.next
        node.data = nextNode.data
        node.next = nextNode.next
        sList.size -= 1

    deleteNode(targetNode)

    sList.printList()


if __name__ == "__main__":
    Solution1()
