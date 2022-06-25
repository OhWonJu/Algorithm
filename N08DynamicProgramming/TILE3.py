# 타일 공사

# 2 x N 바닥에 대해
# 1 X 2
# 2 X 1
# 사이즈의 타일을 이용해 바닥을 덮는 경우의 수를 구하라.
# 단 비대칭의 경우만 허용


MOD = 100000007


def solution():
    # floor 사이즈에 따라 다르지 않을까?
    # 짝수 -> 전체 경우에서, 반 쪼갰을때의 경우. 중앙 두 줄울 1X2 두개로 덮는 경우를 뺴면?
    # 홀수 -> 중앙 한 줄을 2X1로 덮는 경우

    # 전체 경우의 수에서
    # 대칭을 솎아서 빼는 경우
    floor_size = 6
    cache = [-1] * (floor_size + 1)
    cache[1] = 1
    cache[2] = 2

    symmetry = 0
    for i in range(3, floor_size+1):
        # 남은 사이즈가 1이라면...이전 경우의 수가 최종 경우의 수 겠지.
        cache[i] = (cache[i-1] + cache[i-2]) % MOD

    if floor_size % 2 != 0:
        symmetry = cache[(floor_size // 2)]
    elif floor_size <= 2:
        cache[-1] = 0
    else:
        symmetry = cache[floor_size // 2] + cache[floor_size // 2 - 1]

    print(cache[-1])
    print(cache[-1]-symmetry)


if __name__ == "__main__":
    solution()
