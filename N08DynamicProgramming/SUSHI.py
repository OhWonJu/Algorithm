# PACKING 문제와 유사

# 중복 허용
# 메모이제점션을 위한 공간이 너무 큰게 차이점

# 가격 대비 선호도를 높이는 문제

# 가격이 100 단위로 커지니까.
# 100 나눈걸로 메모이제이션하면고
# 시작이 2500부터니까, 2500 전은 무시

# INPUT
# testCase C
# each case
# 초밥 종류 N 예산 M
# each N
# sushis...cost, needy
# 가격은 20,000이하 100의 배수, 선호도는 20이하 자연수


# OUTPUT
# 선호도의 최대합

import weakref


def solution():
    # testCASE
    number_sushi = 6
    budget = 543975612  # 너무 느랴...
    sushi_list = [(2500, 7), (3000, 9), (4000, 10),
                  (5000, 12), (10000, 20), (15000, 1)]

    # 모든 가격은 100의 배수 이기 때문에 예산을 100으로 나누면 됨
    # 최초 시작 지점이 25인것을 또 알 수 있음.
    # 각 예산별 선호도 최대합을 저장하는 cahce
    budget_cache = [0 for _ in range(budget // 100 + 1)]
    min_cost_sushi = min(sushi_list, key=lambda x: x[0])
    budget_cache[min_cost_sushi[0] // 100] = min_cost_sushi[1]

    for b in range((min_cost_sushi[0] // 100) + 1, (budget // 100) + 1):
        for s in sushi_list:
            if b > s[0] // 100:
                budget_cache[b] = max(
                    budget_cache[b], budget_cache[b-(s[0] // 100)] + s[1])

    print(budget_cache[-1])


def solution2():
    budget = 543975612 // 100
    sushi_list = [(25, 7), (30, 9), (40, 10),
                  (50, 12), (100, 20), (150, 1)]
    # 슬라이딩 윈도 사용하자
    # budget_cache는... budget - sushi cost 니까. budget - 200인 셈. 총 200종류랑 비교를 하겠지?
    budget_cache = [0 for _ in range(202)]  # 만일을 대비해 201
    min_cost_sushi = min(sushi_list, key=lambda x: x[0])
    budget_cache[min_cost_sushi[0] % 201] = min_cost_sushi[1]
    result = 0
    for b in range(min_cost_sushi[0]+1, budget + 1):
        needy = 0
        for s in sushi_list:
            if b >= s[0]:
                needy = max(needy, budget_cache[(b-s[0]) % 201] + s[1])
        budget_cache[b % 201] = needy
        result = max(result, needy)

    print(result)


if __name__ == "__main__":
    solution()
