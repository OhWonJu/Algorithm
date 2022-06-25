# 위에서 아래로
# 리버스 정렬


def solution():
    n = int(input())
    array = []
    for _ in range(n):
        array.append(int(input()))

    array.sort(reverse=True)

    for i in array:
        print(i, end=" ")
    print("")


if __name__ == "__main__":
    solution()
