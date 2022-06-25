# 개미 전사

# 인덱스가 인접하면 안됨.
# 최대값 구하기.

def solution():
    n = int(input())
    DP = [0] * 100
    array = list(map(int, input().split()))
    array = array[0:n]

    # 마지막 창고까지 도착할 때 까지 최고의 약탈 수를 저장하면 된다..
    # 기본 조건
    DP[0] = array[0]
    DP[1] = max(array[0], array[1])
    for i in range(2, n):
        #       이전 창고까지 턴것, 이전전 창고 + 현재 창고
        DP[i] = max(DP[i-1], DP[i-2] + array[i])
    print(DP[n-1])


if __name__ == "__main__":
    solution()
