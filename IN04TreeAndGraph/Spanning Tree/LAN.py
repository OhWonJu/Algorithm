## 근거리 네트워크 문제 ##
# 최소 스패닝 트리 문제 #


import sys
import heapq
import math
input = sys.stdin.readline


def solution():
    #building, cable = map(int, input().split()),
    building = 5
    cable = 2

    graph = [[] for _ in range(building)]

    xPos = [] * building
    yPos = [] * building
    connected = []

    #xPos = list(map(int, input().split()))
    #xPos = xPos[:building]
    #yPos = list(map(int, input().split()))
    #yPos = yPos[:building]

    # for _ in range(cable):
    #  u, v = map(int, input().split())
    #  connected.append((u, v))
    xPos = [-7, -7, 10, -4, 10, ]
    yPos = [6, 8, -5, 3, -4]
    connected = [(0, 4), (4, 3)]

    selected_edges = []
    needLens = 0

    def prim(graph, vector, xPos, yPos, connected):
        INF = int(1e9)
        parent = [-1] * vector  # 해당 vector의 부모 노드
        parent[0] = 0  # start node의 부모는 자기자신
        pQueue = []
        added = [False] * vector  # 스패닝 트리 집합 여부
        distance = [INF] * vector  # 해당 vector를 연결하기 위한 최소 cost
        selected_edges = []
        result = 0
        heapq.heappush(pQueue, (0, 0))  # cost, vector

        for u, v in connected: # 연결된 두 노드를 그래프에 표현
            graph[u].append((v, 0))
            graph[v].append((u, 0))

        while pQueue:
            # 현재 노드를 스패닝 트리에 추가 하기 위한 정보 빼내기
            weight, here = heapq.heappop(pQueue)
            if added[here] == True:  # 근데 이미 추가 된 경우라면 패쓰
                continue

            for i in range(vector):  # 현재 노드랑 다른 모든 노드와의 간선 연결 정보 구하기
                if here == i or added[i] == True:  # 다른 노드가 이미 스패닝 트리 원소라면 패쓰
                    continue
                for v, _ in graph[here]: # 이미 연결된 간선을 추가..
                    if v == i:
                        distance[i] = 0
                        parent[i] = here
                        heapq.heappush(pQueue, (distance[i], i))
                x1 = xPos[here]
                y1 = yPos[here]
                x2 = xPos[i]
                y2 = yPos[i]
                cost = math.sqrt(math.pow(abs(x2-x1), 2) +
                                 math.pow(abs(y2-y1), 2))
                if distance[i] > cost:
                    distance[i] = cost
                    parent[i] = here
                    heapq.heappush(pQueue, (distance[i], i))
            if parent[here] != here:
                selected_edges.append((parent[here], here, weight))
            added[here] = True
            result += weight

        return selected_edges, result

    selected_edges, needLens = prim(graph, building, xPos, yPos, connected)
    print(selected_edges)
    print("{:.10f}".format(needLens))


if __name__ == "__main__":
    solution()
