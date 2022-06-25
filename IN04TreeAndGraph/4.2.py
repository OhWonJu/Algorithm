## 최소 트리 ##

# 오름차순으로 정렬된 배열을 높이가 최소가 되는 BST를 만드는 알고리즘 #

from Tree import BinaryNode as Node


def solution():
    array = [0, 1, 2, 3, 4]

    def createBST(array):
        return createMinimalBST(array, 0, len(array)-1)

    def createMinimalBST(array, start, end):
        #if end < start:
        #    return None
        mid = (start + end) // 2
        node = Node(array[mid])
        node.left = createMinimalBST(array, start=start, end=mid-1) if not mid-1 < start else None
        node.right = createMinimalBST(array, start=mid+1, end=end) if not end < mid+1 else None
        return node

    root = createBST(array)
    root.printPreOrder()
    print()
    root.printInOrder()
    print()
    root.printPostOrder()
    print()


if __name__ == "__main__":
    solution()
