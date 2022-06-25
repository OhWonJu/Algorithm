## 균형 확인 ##
# 이진 트리의 균형을 확인
# 왼쪽 서브 트리와 오른쪽 서브트리의 높이 차이가 최대 1
# 재귀적으로 왼쪽 서브트리와 오른쪽 서브트리의 크기 차이를 확인..
# Error크기 (1이상..)일 떄 종료시키면 최적화 가능

from Tree import BinaryNode as Node

root = Node("root")
a0 = Node("a0", parent=root)
a1 = Node("a1", parent=a0)
a2 = Node("a2", parent=a0)
a3 = Node("a3", parent=a1)

b0 = Node("b0", parent=root)


def solution():
    def check_height(root):
        leftHeight = check_height(root.left) if root.left != None else 0
        rightHeight = check_height(root.right) if root.right != None else 0
        if abs(leftHeight - rightHeight) > 1:
            return False
        return max(leftHeight, rightHeight) + 1
    
    if not check_height(root):
        print("Not balanced")
    else: 
        print("Balanced")


if __name__ == "__main__":
    solution()
