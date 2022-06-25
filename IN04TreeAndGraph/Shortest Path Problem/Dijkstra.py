## Dijkstra Shortest Path Problem Basic ##

import time
import sys
input = sys.stdin.readline


def dijkstra_basic():
    INF = int(1e9)

    #n, e = map(int, input().split())
    #start = int(input())
    #graph = [[] for i in range(n+1)]

    ## TEST INPUT ##
    n = 6
    e = 11
    graph = [[] for _ in range(n+1)]
    start = 1
    graph[1].append((2, 2))
    graph[1].append((3, 5))
    graph[1].append((4, 1))
    graph[2].append((3, 3))
    graph[2].append((4, 2))
    graph[3].append((2, 3))
    graph[3].append((6, 5))
    graph[4].append((3, 3))
    graph[4].append((5, 1))
    graph[5].append((3, 1))
    graph[5].append((6, 2))
    ## -- ##

    visited = [False] * (n + 1)
    distance = [INF] * (n + 1)

    # for _ in range(e):
    #    u, v, w = map(int, input().split())
    #    graph[u].append((v, w))

    # 방문하지 않은 노드 중에서, shortest path를 가진 node의 번호를 반환
    def get_smallest_node():
        # 선형 시간이 걸리게 하는 주범...
        # 매번 distance 배열을 선형 탐색...
        min_value = INF
        index = 0  # 가장 최단 거리가 짧은 노드
        for i in range(1, n+1):
            if distance[i] < min_value and not visited[i]:
                min_value = distance[i]
                index = i
        return index

    def dijkstra(start):
        distance[start] = 0
        visited[start] = True

        for there in graph[start]:
            distance[there[0]] = there[1]

        for _ in range(n-1):
            now = get_smallest_node()  # V x V
            visited[now] = True
            for there in graph[now]:
                cost = distance[now] + there[1]
                if cost < distance[there[0]]:
                    distance[there[0]] = cost

    dijkstra(start)

    for i in range(1, n + 1):
        if distance[i] == INF:
            print("INFINTY")
        else:
            print(distance[i], end=" ")
    print()


if __name__ == "__main__":
    start = time.time()

    dijkstra_basic()

    print("RUNNING TIME: {}".format(time.time()-start))
