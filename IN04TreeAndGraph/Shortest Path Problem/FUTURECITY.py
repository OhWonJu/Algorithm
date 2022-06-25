## 플로이드 워셜 알고리즘 ##

import time
import sys
input = sys.stdin.readline


def solution():
    INF = int(1e9)
    n, e = map(int, input().split())
    graph = [[INF] * (n+1) for _ in range(n+1)]

    # 그래프 초기화
    for here in range(1, n+1):
        for there in range(1, n+1):
            if here == there:
                graph[here][there] = 0
    # 간선 입력
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u][v] = graph[v][u] = 1

    # 기착지, 최종 목적지
    K, X = map(int, input().split())

    for now in range(1, n+1):
        for start in range(1, n+1):
            for end in range(1, n+1):
                graph[start][end] = min(
                    graph[start][end], graph[start][now] + graph[now][end])

    distance = graph[1][K] + graph[K][X]

    if distance >= INF:
        print(-1)
    else:
        print(distance)


if __name__ == "__main__":
    start = time.time()

    solution()

    print("RUNNING TIME: {}".format(time.time()-start))
