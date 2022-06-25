## 후속자 ##
# BST에서 주어진 노드의 '다음' 노드(중위 후속자)를 찾는 알고리즘
# 후속자는 오른쪽 어딘가에 있을 것임
# 경우의 수..
# 오른쪽 하위 트리가 있다면 오른쪽 하위 트리의 가장 왼쪽 터미널..
# 오른쪽 하위 트리가 없다면 부모 노드로 올라감
# 오른쪽이 계속 없어서 트리의 루트까지 올라가는 경우 -> 가장 오른쪽 터미널을 방문한 것이니 종료

from Tree import BinarySearchNode as Node

root = Node(20)
a0 = Node(10, parent=root)
a1 = Node(5, parent=a0)
a2 = Node(15, parent=a0)
a3 = Node(3, parent=a1)
a4 = Node(7, parent=a1)
a5 = Node(17, parent=a2)

b0 = Node(30, parent=root)


def solution():
    # 가장 왼쪽 터미널을 반환...
    def left_most_child(node):
        if node == None:
            return None
        while node.left != None:
            node = node.left
        return node

    def inorder_succ(node):
        # 기저 조건
        if node == None:
            return None
        # 오른쪽 서브트리가 존재
        if node.right != None:
            # 오른쪽 서브노드의 가장 왼쪽 노드를 반환
            return left_most_child(node.right)
        else:
            # 오른쪽 서브트리에 대한 방문이 모두 끝난 경우
            left = node
            parent = left.parent
            # 오른쪽이 아닌 왼쪽에 있을 때까지 위로 올라감.
            while parent != None and parent.left != left:
                left = parent
                parent = parent.parent
            return left

    successor = inorder_succ(root)
    print(successor.data)


if __name__ == "__main__":
    solution()
