# 게임 개발
# dx dy가 90도씩 회전


def solution():
    steps = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}  # 북 동 남 서
    n, m = map(int, input().split())
    maps = []
    visited = [[0] * m for _ in range(n)]
    r, c, look = map(int, input().split())
    for _ in range(n):
        inputs = list(map(int, input().split()))
        maps.append(inputs[0:m])
    visited[r][c] = 1

    def turn_left():
        nonlocal look
        look -= 1
        if look == -1:
            look = 3

    def condition_check(row, col):
        if row >= n or row < 0 or col >= m or col < 0:
            return False
        elif maps[row][col] == 1 or visited[row][col] == 1:
            return False
        return True

    result = 1
    turnCount = 0
    while(True):
        turn_left()
        direction = steps[look]
        dr = r + direction[0]
        dc = c + direction[1]
        if condition_check(dr, dc):
            r = dr
            c = dc
            visited[r][c] = 1
            result += 1
            turnCount = 0
        turnCount += 1

        if turnCount == 4:
            turnCount = 0
            dr = r - direction[0]
            dc = c - direction[1]
            if maps[dr][dc] == 1:
                break
            r = dr
            c = dc
    print(result)


if __name__ == "__main__":
    solution()
