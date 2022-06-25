# 상하좌우


def solution():
    stepType = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

    n = int(input())
    steps = list(map(str, input().split()))

    x = 1
    y = 1

    for s in steps:
        pos = None
        if s in stepType:
            pos = stepType[s]
        dx = x + pos[0]
        dy = y + pos[1]
        if dx < 1 or dx > n or dy < 1 or dy > n:
            continue
        x = dx
        y = dy

    print(x, y)


if __name__ == "__main__":
    solution()
