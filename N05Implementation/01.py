# 왕실의 나이트
# 경우의 수..

def solution():
    steps = [(-1, -2), (1, -2), (-1, 2), (1, 2),
             (-2, -1), (-2, 1), (2, -1), (2, 1)]
    pos = input()
    row = int(pos[1])
    col = ord(pos[0])-96

    result = 0
    for s in steps:
        dx = col + s[1]
        dy = row + s[0]

        if dx > 8 or dx < 1 or dy > 8 or dy < 1:
            continue
        result += 1

    print(result)


if __name__ == "__main__":
    solution()
