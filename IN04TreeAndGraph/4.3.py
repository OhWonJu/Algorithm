## 깊이의 리스트 ##
# 동일 깊이에 있는 노드들을 연결리스트로 연결 해주는 알고리즘
# 전위 순회 or BFS로 해결 가능

from collections import deque
from Tree import BinaryNode as Node

root = Node("root")
a0 = Node("a0", parent=root)
a1 = Node("a1", parent=a0)
a2 = Node("a2", parent=a0)
a3 = Node("a3", parent=a1)

b0 = Node("b0", parent=root)
b1 = Node("b1", parent=b0)
b2 = Node("b2", parent=b0)
b3 = Node("b3", parent=b1)
b4 = Node("b4", parent=b1)
b5 = Node("b5", parent=b3)


def solution1():
    # 전위 순회
    # root->sub left right
    lists = []

    def create_level_linked_list(root, level, lists):
        if len(lists) == level:
            lists.append([])
        lists[level].append(root.data)
        create_level_linked_list(
            root.left, level+1, lists) if not root.left == None else None
        create_level_linked_list(
            root.right, level+1, lists) if not root.right == None else None

    create_level_linked_list(root, 0, lists)
    print(lists)


def solution2():
    lists = []

    def create_level_linked_list(root, lists):
        queue = deque([(0, root)])
        while queue:
            level, node = queue.popleft()
            if len(lists) == level:
                lists.append([])
            lists[level].append(node.data)
            queue.append((level+1, node.left)) if node.left != None else None
            queue.append((level+1, node.right)) if node.right != None else None

    create_level_linked_list(root, lists)
    print(lists)


if __name__ == "__main__":
    #solution1()
    solution2()