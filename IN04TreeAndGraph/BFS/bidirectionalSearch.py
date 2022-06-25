## 미로 탈출을 양방향 탐색으로 구현해본다 ##

import time
from collections import deque


def Test():
    maps = [
        [1, 0, 1, 0, 1, 0],
        [1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
    ]

    n = 5
    m = 6

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 부호 반환
    def sgn(x):
        if(not x):
            return 0
        elif(x > 0):
            return 1
        else:
            return 0
    # 절대값 증가

    def incr(x):
        if(x < 0):
            return x - 1
        return x + 1

    def BFS(sx, sy, ex, ey):
        if(sx == ex and sy == ey):
            return 0

        queue = deque()
        queue.append((sx, sy))
        queue.append((ex, ey))
        maps[sx][sy] = 1
        maps[ex][ey] = -1
        while(queue):
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 종료조건
                if(nx < 0 or nx >= n or ny < 0 or ny >= m):
                    continue
                if(nx == 0 and ny == 0):
                    continue
                if(maps[nx][ny] == 0):
                    continue
                if(maps[nx][ny] == 1):
                    maps[nx][ny] = incr(maps[x][y])
                    queue.append((nx, ny))
                elif(sgn(maps[x][y]) != sgn(maps[nx][ny]) and abs(maps[nx][ny]) != 1):
                    print(maps)
                    return abs(maps[x][y]) + abs(maps[nx][ny])
        print(maps)
        return(-1)

    print(BFS(0, 0, n-1, m-1))


def Solution():
    pass


if __name__ == "__main__":
    start = time.time()

    Test()

    print("RUNNING TIME: {}".format(time.time()-start))
