## 트리 순회 순서 변경 ##

# 주어진 전위, 중위 리스트를 통해 후위 순회를 출력

from Tree import BinaryNode, Node

root = BinaryNode(27)
a0 = BinaryNode(16, parent=root)
a1 = BinaryNode(9, parent=a0)
a2 = BinaryNode(12, parent=a1)
a1.left = None
a1.right = a2

b0 = BinaryNode(54, parent=root)
b1 = BinaryNode(36, parent=b0)
b2 = BinaryNode(72, parent=b0)


def Orders():
    print("preorder: ", end="")
    root.printPreOrder()
    print("")
    print("inorder: ", end="")
    root.printInOrder()
    print("")
    print("postorder: ", end="")
    root.printPostOrder()
    print("")


# 전위 순회의 첫 원소는 루트이다.
# 중위 원소의 루트 왼쪽은 왼쪽 서브트리, 오른쪽은 오른쪽 서브트리이다.
# 전위로 루트를 지정, 루트 왼쪽을 중위로 나눔, 이 정보를 재귀
# 후위 순회는 모든 리프를 순회한 뒤 루트를 순회.

def Solution1():
    #size = int(input("size: "))
    #preorder = input("inorder: ").split(" ")
    #preorder = list(map(int, preorder))
    #inorder = input("inorder: ").split()
    #inorder = list(map(int, inorder))
    #size = 7
    preorder = [27, 16, 9, 12, 54, 36, 72]
    inorder = [9 ,12, 16, 27, 36, 54, 72]

    def printPostOrder(preorder: list, inorder: list):
        nodes = len(preorder)
        if(nodes == 0):
            return
        root = preorder[0]
        subsize = inorder.index(root)
        # basic concept of post order...
        printPostOrder(preorder[1: subsize+1], inorder[:subsize]) # call left sub tree
        printPostOrder(preorder[subsize+1:], inorder[subsize+1:]) # call right sub tree
        print(root, end=" ")

    printPostOrder(preorder, inorder)


if __name__ == "__main__":
    # Orders()
    Solution1()
