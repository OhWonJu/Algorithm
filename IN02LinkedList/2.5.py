## 리스트의 합 ##

from singleLinkedList import SingleLinkedList as LinkedList

xList = LinkedList()
xList.append(7)
xList.append(1)
xList.append(6)
xList.append(1)

yList = LinkedList()
yList.append(5)
yList.append(9)
yList.append(3)

# 리스트의 각 원소를 자연수의 자리수로 취급하여
# 두 리스트의 원소를 합한다.
# BCR O(N + M)


def Solution1():
    def addLists(xList, yList):
        resultList = LinkedList()
        xHead = xList.head
        yHead = yList.head
        upper = 0
        while(True):
            if(xHead == None and yHead == None):
                if(upper > 0):
                    resultList.append(upper)
                break
            if(xHead == None):
                sums = yHead.data + upper
                yHead = yHead.next
            elif(yHead == None):
                sums = xHead.data + upper
                xHead = xHead.next
            else:
                sums = xHead.data + yHead.data + upper
                xHead = xHead.next
                yHead = yHead.next
            upper = sums // 10
            sums %= 10
            resultList.append(int(sums))

        return resultList

    result = addLists(xList, yList)
    result.printList()


# 재귀로 푸는 방법
def Solution2():
    resultList = LinkedList()

    def addLists(xHead, yHead, carry):
        # end point
        if(xHead == None and yHead == None):
            if(carry > 0):
                resultList.append(carry)
            return

        value = carry
        if(xHead != None):
            value += xHead.data
        if(yHead != None):
            value += yHead.data
        resultList.append(value % 10)

        # recursion
        addLists(None if xHead == None else xHead.next,
                None if yHead == None else yHead.next, 
                1 if value >= 10 else 0)

    addLists(xList.head, yList.head, 0)
    resultList.printList()


if __name__ == "__main__":
    # Solution1()
    Solution2()
