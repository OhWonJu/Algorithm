## 회문 ##

from singleLinkedList import SingleLinkedList as LinkedList

test1 = LinkedList()
test1.append("T")
test1.append("E")
test1.append("N")
test1.append("E")
test1.append("T")

test2 = LinkedList()
test2.append("R")
test2.append("O")
test2.append("A")
test2.append("S")


# 주어진 리스트가 회문인지 검사
# palindrome - 거꾸로 읽어도 똑같이 읽어짐
# BCR O(N)
# singleList이고 사이즈를 모르는 경우..
# 리스트의 반을 뒤집어 비교한다.
def Solution1():
    targetList = test1
    slower = targetList.head

    def reverseHarf(faster, counter, trigger, rlist):
        # end point
        nonlocal slower
        if(faster.next == None):
            return

        if(counter == 2):
            slower = slower.next
            counter = 0
        faster = faster.next
        counter += 1
        # recursion
        reverseHarf(faster, counter, trigger, rlist)
        if(faster == slower):
            trigger = 1
            return
        elif(trigger == 1):
            return
        rlist.append(faster.data)

    reversList = LinkedList()
    reverseHarf(targetList.head, 0, -1, reversList)

    def isPalindrome(origin, revers):
        while(True):
            if(origin.data != revers.data):
                return False
            elif(revers.next == None):
                return True
            else:
                origin = origin.next
                revers = revers.next
    print(isPalindrome(targetList.head, reversList.head))


# 순환적 접근법
# 스택을 이용한 절반 뒤집기
# 연결 리스트의 길이를 모르는 경우 runner 기법 사용
def Solution2():
    targetList = test2

    def isPalindrome(head):
        fast = slow = head
        stack = []
        # 원소의 수가 홀수인지, 짝수인지에 따라 종료 조건 충족이 달라짐.
        while(fast != None and fast.next != None):
            stack.append(slow.data)
            slow = slow.next
            fast = fast.next.next

        # 원소의 개수가 홀수 개라면 가운데 원소를 넘긴다.
        if(fast != None):
            slow = slow.next

        while(slow != None):
            top = stack.pop()
            if(top != slow.data):
                return False
            slow = slow.next
        return True

    print(isPalindrome(targetList.head))


# 재귀적 접근법
# 연결 리스트의 길이를 아는 경우
# 원소를 절반 위치까지 이동.
# 회문 결과, 다음 비교 원소 class를 반환
def Solution3():
    class Result:
        def __init__(self, node, result):
            self.node = node
            self.result = result

    testList = test2

    def isPalindrome(testList):
        lenght = testList.size
        p: Result = isPalindromeRecurse(testList.head, lenght)
        return p.result

    def isPalindromeRecurse(head, lenght):
        # 원소수가 짝수일 경우
        if(head == None or lenght <= 0):
            return Result(head, True)
        # 홀수인 경우
        elif(lenght == 1):
            return Result(head.next, True)

        # recursion
        res:Result = isPalindromeRecurse(head.next, lenght-2)

        # 회문 여부가 Fasle라면 Fasle 결과를 계속 반환
        if(not(res.result) or res.node == None):
            return res
        
        res.result = (head.data == res.node.data)
        res.node = res.node.next

        return res
    
    print(isPalindrome(testList))



if __name__ == "__main__":
    # Solution1()
    #Solution2()
    Solution3()
