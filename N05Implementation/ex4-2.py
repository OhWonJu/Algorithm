# 시각
# 00시 00분 00초에서 # N시 59분 59초 까지 3이 포함되는 경우의 수는?
# 24 * 59 * 59의 경우의 수 -> 83,544  100만 개 이하이니 3중 for문으로도 가능...
def solution():
    pass
    N = int(input())

    result = 0
    for h in range(N+1):
        for m in range(60):
            for s in range(60):
                # 파이썬 문법.....
                if '3' in str(h) + str(m) + str(s):
                    result += 1
    print(result)


if __name__ == "__main__":
    solution()
