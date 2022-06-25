# 임의의 BST 구현하기
# BST를 BASIC부터 구현하기
# 야 트립도.. BST자너..

import random
from Treap import *

# 루트 이하의 모든 노드를 같은 확률로 선택하는 method


def getRandomNode1(root: Node):
    # option1 느리지만 동작하는
    # 모든 노드를 배열에 복사한 뒤 임의의 원소 반환.
    # 바닥부터 구현하라는 요건을 무시하는 형식...
    # 트리의 구조를 활용해야 함.
    # O(N)의 시간, 공간복잡도.

    def get_values(root):
        if root == None:
            return
        get_values(root.left)
        values.append(root)
        get_values(root.right)

    values = []
    get_values(root)
    rndIndex = random.randrange(0, root.size)
    print(values[rndIndex].data)


def getRandomNode2(root: Node):
    # option6 빠르게 동작하는
    # root의 선택확률 1/N
    # left로 이동할 확률 left size * 1 / N
    # right로 이동할 확률 right size * 1 / N
    # O(logN)
    leftSize = root.left.size if root.left != None else 0
    rndIndex = random.randrange(0, root.size)

    # 왼쪽 서브트리가 선택될 확률
    if rndIndex < leftSize:
        return getRandomNode2(root.left)
    elif rndIndex == leftSize:
        return root
    else:
        return getRandomNode2(root.right)

def getRandomNode3(root: Node):
    # option7 빠르게 동작하는 
    # option6의 재귀 비용울 줄여보자.
    


if __name__ == "__main__":
    root = Node(20)
    root = insert(root, Node(10))
    root = insert(root, Node(30))

    root = insert(root, Node(5))
    root = insert(root, Node(15))

    root = insert(root, Node(3))
    root = insert(root, Node(7))
    root = insert(root, Node(17))

    #getRandomNode1(root)
    #result = getRandomNode2(root)
    #print(result.data)