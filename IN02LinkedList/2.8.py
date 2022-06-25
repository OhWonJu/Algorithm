## 루프 발견 ##

from singleLinkedList import SingleLinkedList as LinkedList

case1 = LinkedList()
case1.append(3)
case1.append(1)
case1.append(5)
case1.append(9)
case1.append(2)
case1.append(1)
case1.append(7)
case1.append(2)
case1.append(6)
case1.tail.next = case1.selectNodeWithIndex(3)

case2 = LinkedList()
case2.append(4)
case2.append(6)
case2.append(3)
case2.append(2)
case2.append(8)

# 해시테이블을 이용한 해결
# 시간복잡도 O(N)


def Solution1():
    def isCircularList(head):
        table = {}
        while(True):
            if(head == None):
                return None
            key = str(head)
            if(not key in table):
                table[key] = True
            elif(table[key] == True):
                return head
            head = head.next

    print(isCircularList(case1.head))


# Runner 기법을 이용한 해결
# 시간복잡도 O(N), 공간복잡도 O(1)
# circuler 인 것은 확인했지만 어느 지점에서 순환이 시작되는지는..?
# slower가 루프에 진입한 순간은 루프가 아닌 노드의 수 k 만큼 이동했을 때이다.
# faster는 이 때 2k만큼 이동했음.
# 즉 slower가 루프에 도착했을 때, faster는 루프에서 roop size % k번 위치에 있음 (K)
# roop Size-K 번 이동하면 두 러너는 만나게 됨.
# 두 러너는 루프의 시작에서 K번 떨어져있게 됨
# 두 러너중 하나를 첫 노드, 하나는 그자리.
# 두 러너가 만나게 되는 곳이 루프의 시작점.
def Solution2():
    def isCircularList(head):
        faster = slower = head
        while(True):
            if(faster != None and faster.next != None):
                faster = faster.next.next
                slower = slower.next
                if(faster == slower):
                    break
            else:
                return None
        slower = head
        while(slower != faster):
            faster = faster.next
            slower = slower.next
        return slower

    print("CircularPoint: ", isCircularList(case1.head))


if __name__ == "__main__":
    print("result circularPoint: ", case1.selectNodeWithIndex(3))
    # Solution1()
    Solution2()
