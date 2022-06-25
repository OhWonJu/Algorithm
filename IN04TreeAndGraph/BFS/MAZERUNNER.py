## 미로 탈출 ##

# N X N 경로 탐색 (0, 0) to (N, M)
# 경로탐색은 BFS!
# 최단 경로의 길이 출력

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

    def BFS(x, y):
        queue = deque([(x, y)])
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
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
        print(maps)
        return(maps[n-1][m-1])

    print(BFS(0, 0))


def Solution():
    pass


if __name__ == "__main__":
    start = time.time()

    Test()

    print("RUNNING TIME: {}".format(time.time()-start))
