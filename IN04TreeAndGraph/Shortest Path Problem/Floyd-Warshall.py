## Floyd-Warshall Alogrithm ##

import time
import sys
input = sys.stdin.readline


def floyd_warshall_path():
    INF = int(1e9)

    #n = int(input())
    #e = int(input())
    #graph = [[INF] * (n + 1) for _ in range(n+1)]

    n = 4
    e = 7
    graph = [[INF] * (n + 1) for _ in range(n+1)]

    for here in range(1, n + 1):
        for there in range(1, n + 1):
            if here == there:
                graph[here][there] = 0

    graph[1][2] = 4
    graph[1][4] = 6
    graph[2][1] = 3
    graph[2][3] = 7
    graph[3][1] = 5
    graph[3][4] = 4
    graph[4][3] = 2

    # for _ in range(e):
    #    u, v, w = map(int, input().split())
    #    graph[u][v] = w

    # 최소 경로 저장 # 추가공간 O(N^2)가 필요함..
    via = [[-1] * (n+1) for _ in range(n+1)]
    path = []
    #

    for now in range(1, n+1):
        for start in range(1, n+1):
            # 최적화
            if graph[start][now] == INF:
                # 기착점까지 가는 경로가 없다면 for문을 돌 이유가 없다..
                continue
            for end in range(1, n+1):
                # 최소 경로 저장
                if(graph[start][end] > graph[start][now] + graph[now][end]):
                    # 해당 경로의 기착지를 저장
                    via[start][end] = now

                graph[start][end] = min(
                    graph[start][end], graph[start][now] + graph[now][end])

    # 최소 경로 재귀적 방법으로 불러오기
    def reconstruct(start, end, path: list):
        # 기저 사례
        if(via[start][end] == -1):
            # 기착지가 없는 경우..
            path.append(start)
            if(start != end):
                path.append(end)
        else:
            # 재귀를 통해 터미널 단계까지 내려가는 것 
            # 최소 단위가 start - way - end 이렇게 인 경우이거나, start-end인 경우 까지 내려가는 것
            w = via[start][end]
            reconstruct(start, w, path)
            path.pop() # w가 중복으로 들어가게 됨.. 그래서 pop
            reconstruct(w, end, path)

    for start in range(1, n+1):
        for end in range(1, n+1):
            if graph[start][end] == INF:
                print("INFINITY")
            else:
                print(graph[start][end], end=" ")
        print()

    reconstruct(1, 3, path)
    print(path)


if __name__ == "__main__":
    start = time.time()

    floyd_warshall_path()

    print("RUNNING TIME: {}".format(time.time()-start))
