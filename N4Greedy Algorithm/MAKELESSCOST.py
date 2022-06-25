# 만들 수 없는 금액

# 입력
# N(1,000)
# N개의 화폐들(1,000,000)

# 출력
# 입력된 동전으로 만들 수 없는 양의 정수 중 최소값을 구하기


def solution():
    N = int(input())
    coins = list(map(int, input().split()))
    coins = coins[:N]
    coins.sort()

    makeless = 1
    for c in coins:
        if makeless < c:
            break
        makeless += c

    print(makeless)


if __name__ == "__main__":
    solution()
