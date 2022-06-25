## 첫 번째 공통 조상 ##
# 두 노드의 첫 공통 조상을 찾는 문제
# 부모 노드에 대한 link가 있는 경우
# 부모 노드에 대한 link가 없는 경우

from Tree import BinaryNode as Node

root = Node(20)
a0 = Node(10, parent=root)
a1 = Node(5, parent=a0)
a2 = Node(15, parent=a0)
a3 = Node(3, parent=a1)
a4 = Node(7, parent=a1)
a5 = Node(17, parent=a2)

b0 = Node(30, parent=root)


# 부모노드에 대한 link가 있는 경우
# 첫 서브 트리를 거슬러 올라가며 그래프를 만듦
# 그 그래프에 두번째 서브트리를 대조
def solution1():
    # 해쉬 테이블 사용
    # 시간복잡도 O(N + M).... 쓸 때 없이 최초 부모 이상으로 올라감..
    def depth(node):
        d = 0
        n = node
        while n.parent != None:
            n = n.parent
            d += 1
        return d

    def set_nodes(nodeA, nodeB):
        if depth(nodeA) < depth(nodeB):
            return nodeA, nodeB
        else:
            return nodeB, nodeA

    def find_parent(first, second):
        visited = {}

        # O(first.depth)
        while first != None:
            visited[first] = True
            first = first.parent

        # O (second.depth)
        while second != None:
            if second in visited:
                return second
            else:
                second = second.parent

    first, second = set_nodes(a3, a2)
    parent = find_parent(first, second)
    print(parent.data)


def solution2():
    # 두 노드에서 둘이 만날 때 까지 올라가는 방식
    # 시간복잡도 O(depth)
    # 터미널과 루트가 주어지면 최악의 경우가 발생
    def depth(node):
        d = 0
        n = node
        while n.parent != None:
            n = n.parent
            d += 1
        return d

    def get_delta(nodeA, nodeB):
        return depth(nodeA) - depth(nodeB)

    def go_up_by(node, delta):
        while(delta > 0 and node != None):
            node = node.parent
            delta -= 1
        return node

    def coommon_ancestor(nodeA, nodeB):
        delta = get_delta(nodeA, nodeB)
        shallower = nodeB if delta > 0 else nodeA
        depther = nodeA if delta > 0 else nodeB
        print(shallower.data)
        print(depther.data)
        # delta 차이를 맞춰주기
        depther = go_up_by(depther, abs(delta))

        while shallower != depther and shallower != None and depther != None:
            # 같은 높이에서 동시에 올라가다보면 공통 부모를 찾을 수 있게 됨
            shallower = shallower.parent
            depther = depther.parent
        return shallower

    parent = coommon_ancestor(a3, a2)
    print(parent.data)


def solution3():
    # depther를 거슬러 올라가며 형제 노드인지 확인
    # 더 나은 worst case time complexity
    def covers(root, p):  # root 이하에 p가 있는지 찾는다.
        if root == None:
            return False
        if root == p:
            return True
        return covers(root.left, p) or covers(root.right, p)

    def get_sibling(node):
        if node == None or node.parent == None:
            return None
        parent = node.parent
        return parent.right if parent.left == node else parent.left

    def common_ancestor(root, p, q):
        # 동일 트리 내에 있는지, 다른 하나를 이미 덮고 있는지
        if not covers(root, p) or not covers(root, q):
            return None
        elif covers(p, q):
            return p
        elif covers(q, p):
            return q

        sibling = get_sibling(p)
        parent = p.parent
        while not covers(sibling, q):
            sibling = get_sibling(parent)
            parent = parent.parent
        return parent

    ancestor = common_ancestor(root, a3, a2)
    print(ancestor.data)

# 부모에 대한 link가 없는 경우
# root에서부터 내려간다.
# 두 노드가 루트로부터의 방향이 달라지면 그 루트가 최초의 공통 부모이다.
def solution3():
    def covers(root, node):
        if root == None:
            return None
        if root == node:
            return True
        return covers(root.left, node) or covers(root.right, node)

    def find_ancestor(root, nodeA, nodeB):
        ancestor = None
        if covers(root.left, nodeA) and covers(root.left, nodeB):
            ancestor = find_ancestor(root.left, nodeA, nodeB)
        elif covers(root.right, nodeA) and covers(root.right, nodeB):
            ancestor = find_ancestor(root.right, nodeA, nodeB)
        else:
            return root
        return ancestor

    def common_ancestor(root, nodeA, nodeB):
        if not covers(root, nodeA) or not covers(root, nodeB):
            return None
        elif covers(nodeA, nodeB):
            return nodeA
        elif covers(nodeB, nodeA):
            return nodeB
        return find_ancestor(root, nodeA, nodeB)

    ancestor = common_ancestor(root, a3, a2)
    print(ancestor.data)


if __name__ == "__main__":
    solution3()
