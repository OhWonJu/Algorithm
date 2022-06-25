## 다익스트라 응용 문제 ##

# distance 관련 식이 합이 아닌 곱이라면?? #

import time
import sys
import heapq

input = sys.stdin.readline

def solution():
    INF = int(1e9)

    case = int(input())
    for _ in range(case):
        #node, edge = map(int, input().split())
        #graph = [[] for _ in range(node+1)]
        #distance = [INF] * (node+1)

        # for _ in range(edge):
        #    u, v, w = map(float, input().split())
        #    u = int(u)
        #    v = int(v)
        #    graph[u].append((v, w))

        node = 7
        edge = 14
        graph = [[] for _ in range(node+1)]
        distance = [INF] * (node+1)

        graph[1].append((2, 1.3))
        graph[1].append((3, 1.1))
        graph[1].append((4, 1.24))
        graph[4].append((5, 1.17))
        graph[4].append((6, 1.24))
        graph[4].append((2, 2))
        graph[2].append((3, 1.31))
        graph[2].append((3, 1.26))
        graph[2].append((5, 1.11))
        graph[2].append((6, 1.37))
        graph[6].append((5, 1.24))
        graph[5].append((7, 1.77))
        graph[6].append((7, 1.11))
        graph[3].append((7, 1.2))

        def dijkstra(start=1):
            pQueue = []
            heapq.heappush(pQueue, (1, start))
            distance[start] = 1
            while pQueue:
                dist, now = heapq.heappop(pQueue)
                if distance[now] < dist:
                    continue
                for edge in graph[now]:
                    cost = dist * edge[1]
                    if cost < distance[edge[0]]:
                        distance[edge[0]] = cost
                        heapq.heappush(pQueue, (cost, edge[0]))

        dijkstra(1)

        if distance[-1] == INF:
            print("INFINITY")
        else:
            print("{:.10f}".format(distance[-1]))


if __name__ == "__main__":
    start = time.time()

    solution()

    print("RUNNING TIME: {}".format(time.time() - start))
