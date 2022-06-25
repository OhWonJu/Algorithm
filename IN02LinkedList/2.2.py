
## 뒤에서 k번째 원소 구하기 ##

from singleLinkedList import SingleLinkedList as LinkedList

sList = LinkedList()
sList.append(1)
sList.append(2)
sList.append(3)
sList.append(4)
sList.append(5)
sList.append(6)

# 재귀적 해결 -> 직관적 #
# 재귀의 끝에서 카운트값을 증가
# 카운트 값이 k가 되면 해당 원소 반환
# 시간복잡도 O(N) 공간복잡도 O(N)
def Solution1():
    k = input("k: ")

    i = 0

    def nToLast(head, k):
        nonlocal i
        # 기저 조건
        if head == None:
            return None

        resultNode = nToLast(head.next, k)
        i += 1
        if int(k) == i:
            return head

        return resultNode

    targetNode = nToLast(sList.head, k)
    printResult(targetNode)

# 비재귀적 해결 -> 비직관적, 좀 더 최적#
# Runner 기법 활용
# 시간복잡도 O(N) 공간복잡도 O(N)
# Runner가 k번 이동 한 뒤 원래 iter를 이동
# Runner가 리스트의 마지막에 위치하면 iter를 반환
def Solution2():
    k = int(input("k: "))

    def nToLast(head, k):

        faster = slower = head

        while True:
            if faster == None:
                if k > 0:
                    print("Index over range!")
                    return None
                break
            if k != 0:
                k -= 1
            else:
                slower = slower.next
            faster = faster.next

        return slower

    targetNode = nToLast(sList.head, k)
    printResult(targetNode)


def printResult(node):
    if node == None:
        print("Node not exist.")
    else:
        print("Node's data: {}".format(node.data))


if __name__ == "__main__":
    # Solution1()
    Solution2()
