# 우물을 기어오르는 달팽이

# 하루에 비가 올 확률 50%
# 비가 오지 않으면 2m
# 비가 오면 1m 올라감

# 경우의 수로 확률 계산하기.

# 원하는 조합 수 / 전체 조합 수 => 확률!

# 전체 조합 수는 ....확률은 1/2이니까 2^m 임
def solution():
    height = 10
    deadLine = 5
    # 1 / 2^5      32

    # 각 날짜마다 오를 수 있는 경우의 수...
    # 이전 결과만 있으면 됨
    # 올라온 높이값의 중복은 쓸모가 없으니 덮어쓰기 위해 dict 자료형 사용
    days = [{}, {}]
    # 첫날의 기본 값 설정
    days[0][1] = 1
    days[0][2] = 2
    # 목표치 이상 오른것을 저장하기 위해
    count = 0
    # 0일차를 지나 1일차부터 
    for now in range(1, deadLine):  # d
        for key in days[(now-1) % 2]:  # h
            case1 = key+1
            case2 = key+2
            if case1 >= height:
                count += 1
            if case2 >= height:
                count += 1
            days[now % 2][case1] = case1
            days[now % 2][case2] = case2
        # 전날 기록은 더이상 필요없으니 지워준다.
        days[(now-1) % 2].clear()

    print(days)
    print(count / pow(2, deadLine))


if __name__ == "__main__":
    solution()
