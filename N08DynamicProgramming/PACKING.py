# 여행 짐 싸기  --- 배낭 문제 중 한 유형

# 최적해의 원소 리스트 구하기..

# needy를 최대화
# weight를 초과하면 안됨

# INPUT
# CASE N(100) WEIGHT W(1000)
# EACH N
## NAME, WEIGHT(1000), NEEDY(1000)

def solution():
    stuff = 6
    weight = 30
    # name, weight, needy
    stuff_list = [("laptop", 4, 7), ("camera", 2, 10), ("xbox", 6, 6),
                  ("grinder", 4, 7), ("dumbell", 2, 5), ("encyclopedia", 10, 4)]

    # 각 용량 마다의 최대값을 찾으면 되지 않을까?
    weight_cache = [0 for _ in range(weight+1)]
    stuffs = [set() for _ in range(weight+1)]
    max_needy = 39

    min_weight_stuff = min(stuff_list, key=lambda x: x[1])
    weight_cache[min_weight_stuff[1]] = min_weight_stuff[2]  # needy
    stuffs[min_weight_stuff[1]].add(min_weight_stuff)  # stuff

    for w in range(min_weight_stuff[1]+1, weight+1):  # w
        for s in stuff_list:  # s
            # s[1] 가 w보다 크면 걍 패쓰
            # w - s의 무게의 값(최적값)의 정보를 사용
            # weight_cache[w-s[1]] 의 값 + s[2] 가 크다면~
            if s[1] > w or w - s[1] < 0:
                continue
            if weight_cache[w-s[1]] + s[2] > weight_cache[w] and s not in stuffs[w-s[1]]:
                weight_cache[w] = weight_cache[w-s[1]] + s[2]
                stuffs[w] = set(stuffs[w-s[1]])
                stuffs[w].add(s)
                continue
            # if (w > 29):
            #    print("PREV NEEDY | NOW NEEDY | NOW STUFF | PREV STUFF")
            #    print(weight_cache[w-s[1]], weight_cache[w], s, stuffs[w-s[1]])
        # 중복으로 담을 수 없으니 상한은 정해져 있음. 물건을 입력할 때마다 needy값을 더해놓으면 상한을 구할 수 있고
        # 그 상한을 달성하는 케이스가 발생하면 모든 물건이 담겼다고 판단되니까.
        # break가능
        if weight_cache[w] == 39:
            weight_cache[-1] = 39
            stuffs[-1] = stuffs[w]
            break

    print(weight_cache)
    #print(stuffs)
    print(weight_cache[-1], len(stuffs[-1]))
    result = list(map(lambda x: x[0], stuffs[-1]))
    # 언팩
    print(*result)


if __name__ == "__main__":
    solution()
