## Bellman-Ford 응용 ##

# 특정 지점으로 돌아와야하는 문제? #
# 음수 사이클을 돌아 시작점으로 올 수 있는가? #
# 최대 경로와 최단 경로를 모두 구해야함.. #

import time
import sys
input = sys.stdin.readline


def solution():
    INF = int(1e9)

    # case = int(input())

    def floyed_Warshall(vector, graph):
        reachable = graph
        for now in range(vector):
            for start in range(vector):
                for end in range(vector):
                    if reachable[start][now] and reachable[now][end]:
                        reachable[start][end] = True
        return reachable

    def bellman_Ford(start, target, vector, graph):
        min_upper = [INF] * vector
        max_upper = [INF] * vector
        min_upper[start] = 0
        max_upper[start] = 0
        # 완화..
        for _ in range(vector-1):
            for here in range(vector):
                for vec in graph[here]:
                    there = vec[0]
                    min_cost = vec[1]
                    max_cost = -vec[1]
                    min_upper[there] = min(
                        min_upper[there], min_upper[here] + min_cost)
                    max_upper[there] = min(
                        max_upper[there], max_upper[here] + max_cost)

        result = []
        result.append(min_upper[target])
        result.append(abs(max_upper[target]))
        # 음수 사이클 여부 확인..
        # 이미 v-1번 완화 됬음...v번째인데 완화가 된다면 음수 사이클이 있다는 것
        # v-1 반복과 v반복을 분리시킨겁니다유.
        for here in range(vector):
            for there, cost in graph[here]:
                # 현재 노드에 대해 완화가 이루어진다면...? 음수 사이클
                if min_upper[here] + cost < min_upper[there]:
                    print("min: ", min_upper[here] + cost, min_upper[there])
                    if reachable[start][here] and reachable[here][target]:
                        result[0] = "INFINITY"
                if max_upper[here] - cost < max_upper[there]:
                    if reachable[start][here] and reachable[here][target]:
                        result[1] = "INFINITY"
        return result

    galaxy, warm = map(int, input().split())
    graph = [[] for _ in range(galaxy)]

    reachable = [[False] * galaxy for _ in range(galaxy)]
    for here in range(galaxy):
        for there in range(galaxy):
            if here == there:
                reachable[here][there] = True

    for _ in range(warm):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        reachable[u][v] = True

    reachable = floyed_Warshall(galaxy, reachable)
    result = bellman_Ford(0, 1, galaxy, graph)

    if reachable[0][1] == False:
        print("UNREACHABLE")
    else:
        print(result)


if __name__ == "__main__":
    start = time.time()
    solution()
    print("RUNNING TIME: {}".format(time.time() - start))
