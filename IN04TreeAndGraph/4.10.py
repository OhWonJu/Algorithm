## 하위 트리 확인 ##
# 두개의 ** 커다란* 이진트리 T1, T2 가 존재
# T1이 T2보다 훨씬 크다고 할 때, T2가 T1의 하위 트리인지 판별하는 알고리즘.

# 리스트화 해서..
# 부분집합인지 확인..
# 동일 원소위치에서 길이가 같은지
# 같다면 비교...?
# T2의 순회 결과가 T1의 부분 문자열

# 트리의 구조가 다르지만 중위, 전위 순회시 동일한 결과를 내놓는 경우가 있음..
# 전위 순회를 하되 None노드를 표기할 방법을 사용한다.
# 그러면 다른 구조를 확인 할 수 있음

# 두 트리 중 하나가 서브트리인지 확인하는 법
# 둘을 전위순회함 (단 None 노드를 기록할 것)
# 전위 순회 결과를 문자열 비교

from Tree import BinaryNode as Node

root = Node(1)
a0 = Node(2, parent=root)
a1 = Node(4, parent=a0)

b0 = Node(3, parent=root)


def solution1():
    # time complexity O(N+M)
    # space complexity O(N+M)
    # 입력이 많다면 상당히 부담스러움
    def get_preorder(node, orderResult):
        if node == None:
            orderResult.append("X")
            return

        orderResult.append(str(node.data))
        get_preorder(node.left, orderResult)
        get_preorder(node.right, orderResult)

    def contains_tree(tree1, tree2):
        tree1_ordered = []
        get_preorder(tree1, tree1_ordered)
        tree2_ordered = []
        get_preorder(tree2, tree2_ordered)

        tree1_ordered = "".join(tree1_ordered)
        tree2_ordered = "".join(tree2_ordered)

        return tree2_ordered in tree1_ordered

    if contains_tree(root, a1):
        print("TRUE")
    else:
        print("FALSE")


def solution2():
    # T1을 탐색하다 T2의 루트를 발견하면 대조하는 방식
    # O(N + KM)이지만 T1부분트리와 T2의 부분이 틀리면 즉시 종료하기 때문에
    # full O(N + KM)은 아님 (최악의 경우 임)
    # 메모리면에서 solution1 보다 널널함.. O(logN + logM) 서브트리로 갈수록 재귀 스택이 반토막 나서?
    # 평균 수행시간, 메모리면에서는 각각 전체 순회 후 비교보다
    # 서브트리로 내려가면서 같은 시작점을 찾는 방식이 나음
    # 단 최악의 수행 시간면에서는 손해

    def sub_Tree(root1, root2):
        # 서브 트리인지 확인
        if root1 == None:
            # 모집단이 None이면 서브트리일 수 없으니까..
            return False
        elif root1 == root2 and match_tree(root1, root2):
            # 동일 노드를 찾은 경우.. 매칭을 시작
            return True
        # 왼쪽 서브트리로,, 오른쪽 서브트리로,, 재귀
        return sub_Tree(root1.left, root2) or sub_Tree(root1.right, root2)

    def match_tree(root1, root2):
        # 기저조건 말단 노드
        if root1 == None and root2 == None:
            return True
        # 기저 조건을 지나.. 둘중 하나만 None인 경우.. 사이즈가 다르다.
        elif root1 == None or root2 == None:
            return False
        # 왼쪽끼리 비교 오른쪽 끼리 비교
        else:
            return match_tree(root1.left, root2.left) and match_tree(root1.right, root2.right)

    def contains_tree(tree1, tree2):
        if tree2 == None:
            return True
        return sub_Tree(tree1, tree2)

    if contains_tree(root, a1):
        print("TRUE")
    else:
        print("FALSE")


if __name__ == "__main__":
    # solution1()
    solution2()
