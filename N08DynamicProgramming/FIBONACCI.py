# 다이나믹 프로그랴밍으로 최적화 할 수 있는 대표적인 예

# 이전 단계들에 대한 연산이 반복됟다 -> 재귀적으로 내려가야하는 횟수가 늘어난다..
# 이전 연산 기록을 저장해놓는다면 내려갈 필요가 없다 **메모이제이션**

# 다이나믹 프로그래밍을 적용할 수 있는 문제는
# 큰 문제를 작은 문제로 나눌 수 있다
# 작은 문제에서 구한 정답은 큰 문제에 공유 된다..? 같다?
# -> 분할 정복과 다른점은 다이나믹 프로그래밍에서의 문제들은 서로에게 영향을 미친다는 것

FIBO_STEP = 99
# 0 번 인덱스 건너 뛰기
memo = [0] * (FIBO_STEP + 1)

# 탑-다운


def fibonacci(x):
    if x == 1 or x == 2:
        return 1
    # 이미 계산된적이 있다면...? 반환
    if memo[x] != 0:
        return memo[x]
    memo[x] = fibonacci(x-1) + fibonacci(x-2)
    return memo[x]


print(fibonacci(FIBO_STEP))


# 반복적 동적 계획법 바텀-업
# 슬라이싱 윈도
cache = [None] * 3
cache[0] = 0  # 0항
cache[1] = 1  # 1항

for i in range(2, FIBO_STEP+1):
    memo[i % 3] = memo[(i-2 % 3)] + memo[(i-1) % 3]

print(memo[FIBO_STEP])


# 반복적 동적 계획법
# 행렬 거듭제곱을 이용한 동적 계획법 으음,.,,
cache = [None] * 3
cache[0] = 0
cache[1] = 1
