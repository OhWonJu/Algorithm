## 음료수 얼려먹기 ##

# N x M
# 그래프의 컴포넌트 수 구하기 -> DFS

import time


def Test():
    plate = [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]
    visited = [False] * len(plate) * len(plate[0])

    def DFSAll(n, m):
        count = 0
        for i in range(len(visited)):
            if(not visited[i]):
                x = i // m
                y = i % m
                if(plate[x][y] != 1):
                    DFS(x, y, n, m)
                    count += 1
        return count

    def DFS(x, y, n, m):
        # 기저 조건
        if(x < 0 or y < 0 or x >= n or y >= m):
            return
        if(plate[x][y] == 1):
            return
        if(not visited[m*x + y]):
            visited[m*x + y] = True
            DFS(x-1, y, n, m)
            DFS(x+1, y, n, m)
            DFS(x, y-1, n, m)
            DFS(x, y+1, n, m)

    result = DFSAll(len(plate), len(plate[0]))

    print(result)


def Solution():
    n, m = map(int, input().split())

    plate = []
    for i in range(n):
        plate.append(list(map(int, input())))

    visited = [False] * n * m

    def DFSAll(n, m):
        count = 0
        for i in range(len(visited)):
            if(not visited[i]):
                x = i // m
                y = i % m
                if(plate[x][y] != 1):
                    DFS(x, y, n, m)
                    count += 1
        return count

    def DFS(x, y, n, m):
        # 기저 조건
        if(x < 0 or y < 0 or x >= n or y >= m):
            return
        if(plate[x][y] == 1):
            return
        if(not visited[m*x + y]):
            visited[m*x + y] = True
            DFS(x-1, y, n, m)
            DFS(x+1, y, n, m)
            DFS(x, y-1, n, m)
            DFS(x, y+1, n, m)

    result = DFSAll(n, m)

    print(result)


if __name__ == "__main__":
    start = time.time()
    Solution()

    print("RUNNING TIME: {}".format(time.time()-start))
