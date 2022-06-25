## 다익스트라 알고리즘 응용 ##

# 시작점이 여러개인 경우 ..? #

import time
import sys
import heapq

input = sys.stdin.readline


def solution():
    INF = int(1e9)

    #case = int(input())
    #node, edge, f, s = map(int, input().split())
    #graph = [[] for _ in range(0, node+1)]
    #distance = [INF] * (node + 1)

    #for _ in range(edge):
    #    u, v, w = map(int, input().split())
    #    graph[u].append((v, w))

    #firedPlace = list(map(int, input().split()))
    #stations = list(map(int, input().split()))

    node = 8; edge = 12; f = 3; s = 2
    graph = [[] for _ in range(0, node + 1)]
    distance = [INF] * (node + 1) 
    graph[1].append((2,3)); graph[2].append((1,3)) 
    graph[1].append((6,9)); graph[6].append((1,9))
    graph[2].append((3,6)); graph[3].append((2,6))
    graph[3].append((4,4)); graph[4].append((3,4))
    graph[3].append((5,2)); graph[5].append((3,2))
    graph[4].append((5,7)); graph[5].append((4,7))
    graph[6].append((5,5)); graph[5].append((6,5))
    graph[8].append((6,5)); graph[6].append((8,5))
    graph[6].append((7,3)); graph[7].append((6,3))
    graph[8].append((7,3)); graph[7].append((8,3))
    graph[7].append((5,1)); graph[5].append((7,1))
    graph[2].append((8,3)); graph[8].append((2,3))

    firedPlace = [2, 3, 5] 
    stations = [4, 6]

    # 일반적인 방식으론 해결 불가능.
    # 1. start를 불난 지점으로 한다
    # 2. 각 소방서에서 불난 지점의 최단거리를 구한다.
    # 3. 플로이드 워셜을 사용한다
    # ==> 여러번 다익스트라를 호출하던가, 플로이드 워셜을 쓰던가임...시간복잡도가 기준치를 넘기게 됨..#
    # 가상의 지점에서 한 번의 다익스트라를 호출하면?
    # 가상의 지점을 만들고 모든 소방서와의 가중치를 0으로 둔다.. = 모든 소방소에서 동시에 다익스트라를 호출하는 격
    # 동시에 시작하게끔 하는 것이 포인트 

    # 가상의 vector에서 모든 소방서로의 edge를 추가
    for i in range(s):
        graph[0].append((stations[i], 0))
    
    def dijkstra(start=0):
        pQueue = []
        heapq.heappush(pQueue, (0, start))
        distance[start] = 0

        while pQueue:
            dist, now = heapq.heappop(pQueue)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]] or cost == 0:
                    distance[i[0]] = cost
                    heapq.heappush(pQueue, (cost, i[0]))

    dijkstra(0)

    result = 0
    for i in range(f):
        result += distance[firedPlace[i]]

    if result >= INF:
        print("INFINITY")
    else:
        print(result)


if __name__ == "__main__":
    start = time.time()

    solution()

    print("RUNNING TIME: {}".format(time.time() - start))
