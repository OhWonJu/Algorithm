# 삼각형 위의 최대 경로

# 각 부분 경로의 최대치를 상위 문제에서 사용한다.


from copy import copy


n = 5
triangle = [[6],
            [1, 2],
            [3, 7, 4],
            [9, 4, 1, 7],
            [2, 7, 5, 9, 4]]

# 마지막 줄은 저장할 필요 없지..
cache = [[-1 for _ in range(x)] for x in range(1, len(triangle))]
# cache = [[-1] * n] * n  # 이 방식과
# cache = [[-1 for _ in range(n)] for _ in range(n)] # 이 방식의 차이로 로직 에러가 나냐 안나냐가 발생함....
# 두 구문의 차이가 뭘까?
# 생성된 결과는 같은데..

# 짐작대로...
# cache = [[-1] * n] * n 의 경우 새로운 배열을 만드는게 아니라 같은 행을 복사하게 되는것..
# 각 인덱스가 같은 메모리를 참조하고 있는거다...


def path(y, x):
    # 재귀 동적 계획법
    # 기저 조건
    # 끝에 다달은 경우
    if y == n - 1:
        return triangle[y][x]
    # 지금까지의 부분 경로 합이 존재할 경우
    if cache[y][x] != -1:
        return cache[y][x]
    cache[y][x] = max(path(y+1, x), path(y+1, x+1)) + triangle[y][x]
    return cache[y][x]
# 시간복잡도 부분문제의 수 O(N^2)  X 문제당 계산 시간 (상수)


print(path(0, 0))


# 반복적 동적 계획법
# 부분 문제 간의 의존성을 파악하기 쉬울 경우 반복문을 이용해서 동적 계획법을 구현 할 수 있다..
# 각 스탭마다 이동 칸 수 가 다른건 조금 힘들지...
n = 5
triangle = [[6],
            [1, 2],
            [3, 7, 4],
            [9, 4, 1, 7],
            [2, 7, 5, 9, 4]]


def path(y, x):
    # 슬라이딩 윈도
    # n을 계산하기 위해선.... n+1의 정보만 있으면 되니까
    # 전체 정보를 유지할 필요는 없음.
    cache = [[-1 for _ in range(n)] for _ in range(2)]
    # 말단 정보 입력 (기저 조건)
    # for i in range(0, n):
    #    cache[(n-1) % 2][i] = triangle[n-1][i]
    #    print(cache[(n-1)%2][i])
    cache[(n-1) % 2] = copy(triangle[n-1])
    for row in range(n-2, -1, -1):
        for col in range(0, row+1):
            cache[row % 2][col] = max(
                cache[(row+1) % 2][col], cache[(row+1) % 2][col+1]) + triangle[row][col]
    return cache[y][x]


print(path(0, 0))
