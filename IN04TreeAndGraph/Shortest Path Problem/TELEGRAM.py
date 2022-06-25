## 한 지점에서 모든 지점으로 ##

import time
import sys
import heapq
input = sys.stdin.readline


def solution():
    INF = int(1e9)

    node, edge, start = map(int, input().split())
    graph = [[] for _ in range(node+1)]
    distance = [INF] * (node+1)

    for _ in range(edge):
        here, there, cost = map(int, input().split())
        graph[here].append((there, cost))

    def dijkstra(start):
        pQueue = []
        heapq.heappush(pQueue, (0, start))
        distance[start] = 0

        while pQueue:
            dist, now = heapq.heappop(pQueue)
            if distance[now] < dist:
                continue
            for there in graph[now]:
                cost = dist + there[1]
                if cost < distance[there[0]]:
                    distance[there[0]] = cost
                    heapq.heappush(pQueue, (cost, there[0]))

    dijkstra(start)

    received_city = 0
    max_delivery_time = 0

    for i in distance:
        if i < INF:
            received_city += 1
            max_delivery_time = max(i, max_delivery_time)

    print(received_city - 1, max_delivery_time)


if __name__ == "__main__":
    start = time.time()

    solution()

    print("RUNNING TIME: {}".format(time.time()-start))