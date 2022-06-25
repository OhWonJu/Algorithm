# 원주율 외우기

# 난이도 합 최소화
# 각 길이 만큼 끊고
# 그 이후의 최적값과
# 끊은 앞 값의 합을 구한다
# 그중 가장 작은 값을 구한다.


INF = int(1e9)


def solution():
    # n = int(input())
    # problem = []
    # for _ in range(n):
    #    problem.append(int(input()))

    data = 12341234

    def classify(start, end):
        d = list(str(data))[start:end]
        d = list(map(int, d))

        print(d)
        if len(set(d)) == 1:
            return 1
        progressive = True
        for i in range(0, len(d)-1):
            if d[i] - d[i+1] != d[0] - d[1]:
                progressive = False
        if progressive and abs(d[0] - d[1]) == 1:
            return 2
        alternating = True
        for i in range(0, len(d)):
            if d[i] != d[i % 2]:
                alternating = False
        if alternating:
            return 4
        if progressive:
            return 5
        else:
            return 10

    cache = [-1 for _ in range(len(str(data)))]

    def memorize(start):
        if start >= len(str(data)):
            return 0
        if cache[start] != -1:
            return cache[start]
        cache[start] = INF
        for L in range(3, 6):
            cache[start] = min(cache[start], memorize(
                start + L) + classify(start, start+L))
        print(cache[start])
        return cache[start]

    memorize(0)
    print(cache)
    print(cache[0])


def solution2():
    # 반복 동적계획법
    # 이전 단계들의 결과를 활용해야함.
    # 3개씩, 4개씩, 5개씩 묶었을 때의 결과가 필요함
    # cache[3] == 3 cache[4] = 4 cache[5] = 5 길이만큼 끊었을때의 결과를 저장
    # cache[i]는 이때까지 온 결과중의 최소만 가지면됨. 이전에 몇 단계로 묶었는지는 중요하지 않음
    # (3묶음 결과 cache[i] i,,,,i-1,,,,i-2,,,) + cache[i-3], ...중의 최소값..?
    def group_3(a, b, c):
        if a == b == c:
            return 1
        if abs(a-b) == abs(b-c) == 1:
            return 2
        if a == c != b:
            return 4
        if a-b == b-c:
            return 5
        return 10

    def group_4(a, b, c, d):
        if a == b == c == d:
            return 1
        if abs(a-b) == abs(b-c) == abs(c-d) == 1:
            return 2
        if a == c and b == d and a != b:
            return 4
        if a-b == b-c == c-d:
            return 5
        return 10

    def group_5(a, b, c, d, e):
        if a == b == c == d == e:
            return 1
        if abs(a-b) == abs(b-c) == abs(c-d) == abs(c-d):
            return 2
        if a == c == e and b == d and a != b:
            return 4
        if a-b == b-c == c-d == d-e:
            return 5
        return 10

    data = 12341234
    data = list(map(int, (list(str(data)))))
    cache = [None] * (len(data)+1)
    cache[3] = group_3(data[0], data[1], data[2])
    cache[4] = group_4(data[0], data[1], data[2], data[3])
    cache[5] = group_5(data[0], data[1], data[2], data[3], data[4])

    for i in range(6, len(data)+1):
        temp = []
        if cache[i-3] != None:
            temp.append(cache[i-3] + group_3(i, i-1, i-2))
        if cache[i-4] != None:
            temp.append(cache[i-4] + group_4(i, i-1, i-2, i-3))
        if cache[i-5] != None:
            temp.append(cache[i-5] + group_5(i, i-1, i-2, i-3, i-4))
        cache[i] = min(temp)
    print(cache[-1])


if __name__ == "__main__":
    solution2()
