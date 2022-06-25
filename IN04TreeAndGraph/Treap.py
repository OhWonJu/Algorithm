## 트립 구현 ##

# 트립? 균형 잡힌 이진 탐색 트리 구현체 중 하나
# AVL...Red-Black tree는 구현이 어려웡..
# Treap은 상대적으로 구현이 간단

# Treap 은 난수에 의해 원소의 추가 순서가 정해짐.. 일종의 랜덤 이진트리
# 새 Node가 추가 될 때 마다 해당 Node에 Priority를 부여함
# 부모의 Priority가 자식보다 높도록 배치함.

# 트립의 조건
# 1. 이진 탐색 트리의 조건
# 2. 힙의 조건 : 모든 노드의 우선순위는 각자의 자식 노드보다 크거나 같다.

import random


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.priority = round(random.random(), 4)
        self.size = 1  # size를 통해 k번째 원소나 k보다 작은 원소를 세는 등의 연산을 편하게 할 수 있다.
        self.left = left
        self.right = right

    def setLeft(self, newNode):
        self.left = newNode
        self.calcSize()

    def setRight(self, newNode):
        self.right = newNode
        self.calcSize()

    def calcSize(self):
        self.size = 1
        if(self.left):
            self.size += self.left.size
        if(self.right):
            self.size += self.right.size
        # print(self.size)


def init(ls):
    root = Node(ls[0])
    for i in range(len(ls)):
        newNode = Node(ls[i])
        root = insert(root, newNode)

    return root

# 노드 추가와 "쪼개기" 연산
# 1. node가 root보다 우선순위가 낮은 경우
# -> 그냥 root하위에 적정 위치에 재귀하여 배치..
# 2. node가 root보다 우선순위가 높은 경우
# -> root 포함 모든 node가 이 node의 자손이 되야함.
# 기준값 보다 작은 서브트리와 큰 서브트리로 쪼개야한다. root가 기준값보다 크냐 작냐에 따라 서브트리를 쪼개는 방향이 달라짐


def split(root: Node, data):
    if(root == None):
        return None, None
    # root 데이터가 큰 경우
    if(root.data > data):
        left, right = split(root.left, data)
        root.setLeft(right)
        return left, root
    # root 데이터가 작은 경우
    left, right = split(root.right, data)
    root.setRight(left)
    return root, right


def insert(root: Node or None, node: Node):
    if(root == None):
        return node
    # node가 root를 대체해야하는 경우 <priority>
    if(root.priority < node.priority):
        left, right = split(root, node.data)
        node.setLeft(left)
        node.setRight(right)
        return node
    # root가 유지되는 경우
    elif(root.data > node.data):
        root.setLeft(insert(root.left, node))
    else:
        root.setRight(insert(root.right, node))
    return root


# 삭제, "합치기" 연산
# 이진 검색트리와 다를게 없음, 단 우선순위를 통해 판별
def merge(nodeA: Node, nodeB: Node):
    # max(a) < min(b)인 경우를 가정
    if(nodeA == None):
        return nodeB
    if(nodeB == None):
        return nodeA
    if(nodeA.priority < nodeB.priority):
        nodeB.setLeft(merge(nodeA, nodeB.left))
        return nodeB
    nodeA.setRight(merge(nodeA.right, nodeB))
    return nodeA


def erase(root: Node, data):
    if(root == None):
        return root
    if(root.data == data):
        ret = merge(root.left, root.right)
        del(root)
        return ret
    if(data < root.data):
        root.setLeft(erase(root.left, data))
    else:
        root.setRight(erase(root.right, data))
    return root


# k번째 원소 찾기
# 왼쪽 subTree의 크기가 l이라 할 때.
# k <= l 해당 노드는 왼쪽 subTree에 있음
# k == l + 1 root가 해당 노드 <-목표
# k > l + 1 해당 노드는 오른쪽 subTree에 존재. 오른쪽 subTree에서 k-l-1 번째 노드가 됨
def kth(root: Node, k: int):
    if(root.size < k):
        return None
    leftSize = 0
    if(root != None):
        if(root.left != None):
            leftSize = root.left.size
        if(k <= leftSize):
            return kth(root.left, k)
        if(k == leftSize + 1):
            return root
        return kth(root.right, k - leftSize - 1)


def eraseKth(root: Node, k: int):
    node = kth(root, k)
    root = erase(root, node.data)
    return root



def countLessThen(root: Node, data):
    if(root == None):
        return 0
    if(root.data >= data):
        return countLessThen(root.left, data)
    leftSize = root.left.size if root.left else 0
    return leftSize + 1 + countLessThen(root.right, data)

def lowerBound(root: Node, data):
    pos = countLessThen(root, data)
    return pos + 1
