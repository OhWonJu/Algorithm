## 우선순위 큐를 사용한 다익스트라 최단거리 ##

# 최단거리 테이블을 사용할 경우 매번 최단거리 테이블을 선형 탐색해야함... #
# 시간복잡도 (V^2)가 되는 이유임..#
# 우선순위 큐를 사용하여 구현 하면 #
# worst case에서도 시간복잡도 (ElogV)를 보장할 수 있다.  거진 반절 #
# 포인트는 최단거리 테이블에서 일일이 찾지 않고 #
# 최단거리 노드를 별도로 저장해놓는것 #

import time
import heapq
import sys
input = sys.stdin.readline


def dijkstra_shortest_path():
    INF = int(1e9)

    #n, e = map(int, input().split())
    #start = int(input())
    #graph = [[] for _ in range(n+1)]
    #distance = [INF] * (n+1)

    # for _ in range(e):
    #    u, v, w = map(int, input().split())
    #    graph[u].append((v, w))

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
    distance = [INF] * (n+1)

    def dijkstra(start):
        pQueue = []
        heapq.heappush(pQueue, (0, start))
        distance[start] = 0

        while pQueue:
            dist, now = heapq.heappop(pQueue)
            if distance[now] < dist:
                # INF가 아니란것은 처리된적이 있는 것..
                # 최단거리 테이블에 기록된 기록이 더 최단거리면 처리할 필요 없음
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(pQueue, (cost, i[0]))

    dijkstra(start)

    for i in range(1, n + 1):
        if distance[i] == INF:
            print("INFINITY")
        else:
            print(distance[i], end=" ")
    print()


if __name__ == "__main__":
    start = time.time()

    dijkstra_shortest_path()

    print("RUNNING TIME: {}".format(time.time()-start))
