class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.children = []
        if(parent != None):
            parent.children.append(self)

    def printLabels(self):
        print(self.data, end=" ")
        if(len(self.children) <= 0):
            print("|")
        for child in self.children:
            child.printLabels()

    def height(self):
        h = 0
        for child in self.children:
            h = max(h, 1+child.height())
        return h


class BinaryNode:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
        if(self.parent != None):
            if(self.parent.left == None):
                self.parent.left = self
            elif(self.parent.right == None):
                self.parent.right = self
            else:
                del(self)

    def printPreOrder(self):
        print(self.data, end=" ")
        self.left.printPreOrder() if self.left != None else None
        self.right.printPreOrder() if self.right != None else None

    def printInOrder(self):
        self.left.printInOrder() if self.left != None else None
        print(self.data, end=" ")
        self.right.printInOrder() if self.right != None else None

    def printPostOrder(self):
        if(self == None):
            return
        self.left.printPostOrder() if self.left != None else None
        self.right.printPostOrder() if self.right != None else None
        print(self.data, end=" ")


class BinarySearchNode:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
        if self.parent != None:
            if self.parent.left == None and self.parent.data >= self.data:
                self.parent.left = self
            elif self.parent.right == None and self.parent.data < self.data:
                self.parent.right = self
            else:
                del self


if __name__ == "__main__":
    root = Node("root")
    a0 = Node("a0", parent=root)
    a1 = Node("a1", parent=a0)
    a2 = Node("a2", parent=a0)
    a3 = Node("a3", parent=a1)
    a4 = Node("a4", parent=a2)

    b0 = Node("b0", parent=root)
    b1 = Node("b1", parent=b0)
    b2 = Node("b2", parent=b0)
    b3 = Node("b3", parent=b1)
    b4 = Node("b4", parent=b1)
    b5 = Node("b5", parent=b3)

    c0 = Node("c0", parent=root)
    c1 = Node("c1", parent=c0)

    root.printLabels()
    print(root.height())
