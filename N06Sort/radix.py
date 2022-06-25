# 기수 정렬

# 낮은 자리수 부터 정렬 하는 방식
# 비교 연산 X
# 하지만 계수 정렬처럼 추가 공간 필요...-> 기수 테이블을(정수라면 0~9) 위한 공간

# 자리수가 고정된 값에 효과적 (수, 문자열)
# 단 자리수가 고정되어있지 않은 값엔 사용불가.

from collections import deque

array = [15, 27, 64, 25, 50, 4, 17, 100, 39, 28]


def radix_sort(array):
    # 0 ~ 9 자리수 표현
    bukects = [deque() for _ in range(10)]
    max_val = max(array)
    queue = deque(array)
    # 기수
    order = 1
    while max_val >= order:
        # 각수를 끝자리에 해당하는 bukect에 배치
        while queue:
            num = queue.popleft()
            # 기수에 따라 자릿수를 하나씩 덜어내고.. 그것의 나머지면... 끝자리를 알 수 있지
            bukects[(num // order) % 10].append(num)
        # bukect에서 순차적으로 popleft
        for bukect in bukects:
            while bukect:
                queue.append(bukect.popleft())
        order *= 10
    return list(queue)

print(radix_sort(array))

# 시간복잡도는 O(R*(N+B))
# 최고 자릿수 * (전체데이터 수 + 버켓수)
