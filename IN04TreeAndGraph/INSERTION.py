## 삽입정렬 뒤집기 ##

# 각 위치에 있는 값들이 움직인 칸수를 통해 원래 수열을 찾아내기
from Treap import *


def Solution():
    shifted = [0, 1, 1, 2, 3]
    n = len(shifted)
    origin = [0 for i in range(n)]
    # 각 원소의 이동 횟수 = 원소보다 큰 수의 개수
    print(shifted)

    candidiates = None
    for i in range(n):
        candidiates = insert(candidiates, Node(i+1))
    for i in range(n-1, -1, -1):
        larger = shifted[i]
        k = kth(candidiates, i + 1 - larger)
        origin[i] = k.data
        candidiates = erase(candidiates, k.data)

    print(origin)


if __name__ == "__main__":
    Solution()
