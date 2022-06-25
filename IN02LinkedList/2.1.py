## 중복 제거 ##

from singleLinkedList import SingleLinkedList as LinkedList
import mergeSort


# 버퍼 사용 #
# 해시테이블을 사용
# 시간복잡도 O(N)
def Solution1():
    ls = [1, 7, 5, 3, 7, 8, 1, 8, 6, 4, 5, 3, 2]

    def deleteDupls(ls):
        table = {}
        tempLs = []
        it = iter(ls)
        for i in range(len(ls)):
            if not(ls[i] in table):
                table[ls[i]] = True
                tempLs.append(next(it))
            else:
                next(it)
        return tempLs

    result = deleteDupls(ls)

    print(result)


# 버퍼 미사용 #

# 정렬을 허용한다면?
# 정렬을 통한 중복 제거
# merge sort 직접 구현 해보자.
# 시간 복잡도 O(N + NlogN)
def Solution2():
    ls = [1, 7, 5, 3, 7, 8, 1, 8, 6, 4, 5, 3, 2]

    def deleteDupls(ls):
        mergeSort.mergeSort(ls)

        i = 0
        while(i+1 < len(ls)):
            if(ls[i] == ls[i+1]):
                del(ls[i+1])
            else:
                i += 1

    deleteDupls(ls)
    print(ls)


# 정렬을 허용하지 않는다면?
# Runner기법 사용
# 시간복잡도 O(N^2)


def Solution3():
    sList = LinkedList()
    sList.append(1)
    sList.append(7)
    sList.append(5)
    sList.append(3)
    sList.append(7)
    sList.append(8)
    sList.append(1)
    sList.append(8)
    sList.append(6)
    sList.append(4)
    sList.append(5)
    sList.append(3)
    sList.append(2)

    def deleteDupls(head):
        current = head
        while(current != None):
            runner = current
            while(runner.next):
                if(runner.next.data == current.data):
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next 

    deleteDupls(sList.head)
    ls = sList.getAll()
    print(ls)


if __name__ == "__main__":
    # Solution1()
    # Solution2()
    Solution3()
