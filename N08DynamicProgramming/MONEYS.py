# 효율적인 화폐 구성

# 조합 문제??
# C(n, k) 순서에 상관 없이 k개의 원소를 선택~~   -- 순열은 순서에 상관이 있음


# 인덱스를 값
# value를 그 값을 만들기 위한 지폐수
# 작은 단위부터 계산해복..

def solution():
    INF = int(1e9)
    # n가지 종류의 화폐를 이용해 그 가치가 M이 되도록 하는 최소한의 수는?
    n, m = map(int, input().split())
    table = [INF] * (m+1)
    money = []
    for _ in range(0, n):
        money.append(int(input()))

    table[0] = 0
    # 각 화폐 단위 마다
    for unit in money:
        for j in range(unit, m+1):
            # 각 (금액 - 단위)에서 찾는다..
            # 현재 금액에서 화폐 단위를 뺸 금액을 구하는 경우가 있다면.
            # 그 뺸 금액 + 해당 화폐 단위가 현재 금액인 것이다.
            if table[j - unit] != INF:
                table[j] = min(table[j], table[j - unit] + 1)

    if table[m] == INF:
        print(-1)
    else:
        print(table[m])


if __name__ == "__main__":
    solution()
