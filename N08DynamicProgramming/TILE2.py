# 타일 공사

# 2 x N 바닥에 대해
# 1 X 2
# 2 X 1
# 사이즈의 타일을 이용해 바닥을 덮는 경우의 수를 구하라.


# 이전 단계에서의 경우의 수는 중요하지 않다!
# 지금 단계를 덮을 수 있는 경우의 수만 구하면 된다.
# 1칸만 남았다면 경우의 수 1
# 2칸이 남았다면 경우의 수는 2
# 이전 단계에서 이걸 더하면 된다!

MOD = 100000007


def solution():
    floor_size = 4
    cache = [-1] * (floor_size + 1)
    cache[1] = 1
    cache[2] = 2

    for i in range(3, floor_size+1):
        # 남은 사이즈가 1이라면...이전 경우의 수가 최종 경우의 수 겠지.
        cache[i] = (cache[i-1] + cache[i-2]) % MOD

    print(cache[-1])


if __name__ == "__main__":
    solution()
