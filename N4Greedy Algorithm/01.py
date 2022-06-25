# 숫자 카드 게임

# min()힘수 사용법
# 2중 for문 활용
# 두가지 방식으로 해결 가능해야함.

def solution():
    INF = int(1e9)
    m, n = map(int, input().split())

    result = -1
    for _ in range(m):
        inputs = list(map(int, input().split()))
        minValue = min(inputs[0:n])
        result = max(minValue, result)

    print(result)

    result = -1
    for _ in range(m):
        inputs = list(map(int, input().split()))
        minValue = INF
        for d in inputs[0:n]:
            minValue = min(d, minValue)
        result = max(result, minValue)

    print(result)


if __name__ == "__main__":
    solution()
