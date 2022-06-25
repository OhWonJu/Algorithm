## BST 검증 ##
# 주어진 이진 트리가 이진 검색 트리인지 확인하는 함수를 작성
# BST 정리를 이용 - 왼쪽 서브트리는 root보다 작고 오른쪽 서브트리는 root보다 크다.
# left <= current < right

# 중위 순회로도 해결 가능. 단 트리 내에 중복된 값이 없는 경우만.
# 중위 순회 결과 -> 정렬된 결과 -> 마지막과 그전 원소간의 대소 관계를 확인하면 됨..

from Tree import BinarySearchNode as Node

root = Node(20)
a0 = Node(10, parent=root)
a1 = Node(5, parent=a0)
a2 = Node(15, parent=a0)
a3 = Node(3, parent=a1)
a4 = Node(7, parent=a1)
a5 = Node(17, parent=a2)

b0 = Node(30, parent=root)
#b1 = Node(13, parent=b0)

def solution():
    def is_bst():
        return check_bst(root, None, None)

    def check_bst(root, minVal, maxVal):
        if root == None:
            return True
        if (minVal != None and minVal > root.data) or (maxVal != None and maxVal <= root.data):
            return False
        if not check_bst(root.left, minVal, root.data) or not check_bst(root.right, root.data, maxVal):
            return False
        return True

    if is_bst():
        print("BST")
    else:
        print("Not")


if __name__ == "__main__":
    solution()
