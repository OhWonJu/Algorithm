# 떡볶이 떡 만들기

# 두 입력 값 중 더 큰 데이터에 맞춰서 이진분할..
# 파라메트릭 서치 유형
import sys
input = sys.stdin.readline


def solution():
    n, h = map(int, input().split())
    dduck = list(map(int, input().split()))
    dduck = dduck[0:n]

    left = 0
    right = max(dduck)
    result = 0
    while left <= right:
        total = 0
        mid = (left + right) // 2
        for d in dduck:
            if d > mid:
                total += d - mid
        # 충분히 긴 경우
        if total >= h:
            left = mid + 1
            result = mid
        else:
            right = mid - 1
    print(result)


if __name__ == "__main__":
    solution()
