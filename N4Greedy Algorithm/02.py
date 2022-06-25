# 1이 될 때 까지

# 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 수행
# N에서 1을 뺀다.
# M을 K로 나눈다.

# N이 1이 될 수 있는 최소 수행횟수를 구하여라.

def solution():
    N, K = map(int, input().split())
    count = 0
    while(True):
        share = N // K
        rest = N % K
        print("share: {}  rest: {}" .format(share, rest))
        if share == 0:
            count += rest-1
            break
        N = share
        count += (1 + rest)
    print(count)


if __name__ == "__main__":
    solution()
