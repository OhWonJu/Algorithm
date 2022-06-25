## 교집합 ##

from singleLinkedList import SingleLinkedList as LinkedList

case1 = LinkedList()
case1.append(3)
case1.append(1)
case1.append(5)
case1.append(9)
case1.append(7)
case1.append(2)
case1.append(1)

case2 = LinkedList()
case2.append(4)
case2.append(6)
case2.connectLists(case1, case1.selectNodeWithIndex(4))

case3 = LinkedList()
case3.append(4)
case3.append(6)
case3.append(7)
case3.append(2)
case3.append(1)

# 주어진 두 리스트가  교집합인지 확인
# 두 연결리스트가 교집합? -> tail node가 같다는 것을 의미.
# 연결 지점을 찾기 위해서는? tail에서부터 동시에 순회하면 분기지점을 찾을 수 있다. singleLinkedList에서는 불가능..
# 동일 길이 지접에서 순회한다면 singleLinkedList에서도 알 수 있다

# tail과 size를 모른다고 가정
# 시간복잡도 O(N + M)
def Solution1():
    def getSizeAndTail(head):
        size = 0
        while(head != None and head.next != None):
            size += 1
            head = head.next
        if(head != None):
            size += 1
        return size, head

    def findIntersectionNode(ls1_size, ls2_size, cs1, cs2):
        longer = shoter = None
        lgSize = shSize = 0

        if(ls1_size >= ls2_size):
            longer = cs1.head
            lgSize = ls1_size
            shoter = cs2.head
            shSize = ls2_size
        else:
            longer = cs2.head
            lgSize = ls2_size
            shoter = cs1.head
            shSize = ls1_size

        while(longer != None and shoter != None):
            if(lgSize != shSize):
                longer = longer.next
                lgSize -= 1
            else:
                if(longer == shoter):
                    return shoter
                longer = longer.next
                shoter = shoter.next
        return None

    ls1_size, ls1_tail = getSizeAndTail(case1.head)
    ls2_size, ls2_tail = getSizeAndTail(case2.head)

    if(ls1_tail == ls2_tail):
        print("Intersection node: ", findIntersectionNode(
            ls1_size, ls2_size, case1, case2))
    else:
        print("Two casees does not intersection")


if __name__ == "__main__":
    Solution1()
