import time
import sys
import heapq
input = sys.stdin.readline

## 음주 운전 단속 ##
# 플로이드-워셜 알고리즘 응용 #
# 간선간의 가중치 + 특정 간선마다의 추가 가중치가 있는 문제 #
# 최단 경로를 찾고 그 경로상의 가장 큰 추가 가중치를 가지고 있는 노드를 찾는 방식은 불가능 #
# 최단거리가 최단거리가 되지 않을 수가 있음을 의미함.. 최악 거리라도 추가 가중치가 없다면...#
# 어떤 정점을 경유하는지가 중요한 문제  == 플로이드 워셜이 유리 #
# 정점의 집합을 늘리는 방식인 셈 #
## 정점의 순서는 상관 없기 때문에 ##
## 추가 가중치가 낮은 순으로 정렬한 뒤 플로이드 워셜을 진행하면 됨 ##

### 정점의 추가 가중치에 대해 고려해야하는 경우!! ###


def solution():
    INF = int(1e9)

    # vector, edge = map(int, input().split())
    vector = 8
    edge = 12
    graph = [[INF] * (vector + 1) for _ in range(vector + 1)]
    weight = [[INF] * (vector + 1) for _ in range(vector + 1)]

    for here in range(1, vector + 1):
        for there in range(1, vector + 1):
            if here == there:
                graph[here][there] = 0

    # delayTime = list(map(int, input().split()))
    delayTime = [8, 6, 5, 8, 3, 5, 8, 4]

    # for _ in range(edge):
    #    u, v, w = map(int, input().split())
    #    graph[u][v] = w
    #    graph[v][u] = w
    graph[1][6] = graph[6][1] = 9
    graph[1][2] = graph[2][1] = 3
    graph[2][8] = graph[8][2] = 3
    graph[6][8] = graph[8][6] = 5
    graph[6][7] = graph[7][6] = 3
    graph[8][7] = graph[7][8] = 3
    graph[6][5] = graph[5][6] = 5
    graph[4][5] = graph[5][4] = 7
    graph[3][4] = graph[4][3] = 4
    graph[3][5] = graph[5][3] = 2
    graph[2][3] = graph[3][2] = 6
    graph[7][5] = graph[5][7] = 1

    # 핵심 #
    order = []
    for i in range(1, vector + 1):
        heapq.heappush(order, (delayTime[i-1], i))

    # case = int(input())
    case = 2
    result = [INF] * case
    # points = []
    # for _ in range(case):
    #    s, t = map(int, input().split())
    #    points.append((s, t))
    points = [(1, 5), (6, 3)]

    for v in range(vector):
        now = order[v][1]
        for start in range(1, vector + 1):
            if graph[start][now] == INF or 0:
                continue
            for end in range(1, vector + 1):
                graph[start][end] = min(
                    graph[start][end], graph[start][now] + graph[now][end])
                weight[start][end] = min(
                    weight[start][end], order[v][0] + graph[start][now] + graph[now][end])

    for i in range(case):
        s, t = points[i]
        result[i] = weight[s][t]

    for r in result:
        if r >= INF:
            print("INFINITY")
        else:
            print(r)


if __name__ == "__main__":
    start = time.time()
    solution()
    print("RUNNING TIME: {}".format(time.time() - start))
