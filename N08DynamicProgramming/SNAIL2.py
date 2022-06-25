# 우물 오르는 달팽이 - 확률이 다르면?

# 비가 올 때 2m 이동
# 비가 안올때 1m 이동
# 비가 올 확률이 75%라면??

# 부분 조합 / 전체 조합이 아니라
# 애초부터 확률을 구하면 됨..

def solution():
    height = 5
    deadLine = 3
    # 1 / 2^5      32

    days = [{}, {}]
    # key는 높이, value는 확률
    days[0][1] = 0.25
    days[0][2] = 0.75

    prob = 0
    for key, value in days[0].items():
        if key >= height:
            prob += value

    for now in range(1, deadLine):  # d
        for key, value in days[(now-1) % 2].items():  # h
            case1_key = key + 1
            case1_value = value*0.25
            case2_key = key + 2
            case2_value = value*0.75
            if case1_key >= height:
                prob += case1_value
            if case2_key >= height:
                prob += case2_value

            if case1_key in days[now%2]:
                days[now%2][case1_key] += case1_value
            else:
              days[now%2][case1_key] = case1_value
            if case2_key in days[now%2]:
                days[now%2][case2_key] += case2_value
            else:
              days[now%2][case2_key] = case2_value
        # 전날 기록은 더이상 필요없으니 지워준다.
        days[(now-1) % 2].clear()

    print(days)
    print(prob)


if __name__ == "__main__":
    solution()


#5 4
#5 3
#4 2
#3 2
#------- 여기사 1뺸갑 ㅅ이 답...
# 0.9960937500
# 0.8437500000
# 0.5625000000
# 0.9375000000