# 부품 찾기

# 이진 탐색
from bisect import *
import sys
input = sys.stdin.readline


def solution1():
    # 이진 분할 라이브러리 bisect 사용
    N = int(input())
    temp = list(map(int, input().split()))
    array = temp[0:N]

    M = int(input())
    temp = list(map(int, input().split()))
    req = temp[0:M]

    array.sort()
    print(array)
    result = []
    for x in range(M):
        # 같은 값이 있는 경우 그 값의 앞 index값을 줌..
        i = bisect_left(array, req[x])
        print(i)
        # x가 존재하고, 인덱스 값에 위치하는 값이 x와 같을 경우..
        if i != len(array) and array[i] == req[x]:
            result.append("YES")
            continue
        result.append("NO")

    print(result)


def solution2():
    # 직접 구현
    def binary_search(array, target, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            return binary_search(array, target, start, mid-1)
        else:
            return binary_search(array, target, mid+1, end)

    N = int(input())
    temp = list(map(int, input().split()))
    array = temp[0:N]

    M = int(input())
    temp = list(map(int, input().split()))
    req = temp[0:M]

    array.sort()
    for x in req:
        index = binary_search(array, x, 0, len(array)-1)
        if index != None:
            print("YES", end=" ")
        else:
            print("NO", end=" ")


def solution3():
    # 계수 정렬을 이용
    # 데이터의 표현 범위는 한정적이라 가능..? <- 사실상 해시테이블 ?
    array = [0] * 100001
    for i in input().split():
        array[int(i)] = 1

    M = int(input())
    temp = list(map(int, input().split()))
    req = temp[0:M]

    for x in req:
        if array[x] == 1:
            print("YES", end=" ")
        else:
            print("NO", end=" ")


def solution4():
    # 배열 내에 특정 수가 한 번이라도 등장했는지를 검사..
    # 집합 자료형을 사용하면 해결 가능 set()

    N = int(input())
    temp = list(map(int, input().split()))
    array = set(temp[0:N])

    M = int(input())
    temp = list(map(int, input().split()))
    req = temp[0:M]

    for x in req:
        if x in array:
            print("YES", end=" ")
        else:
            print("NO", end=" ")


if __name__ == "__main__":
    solution4()
