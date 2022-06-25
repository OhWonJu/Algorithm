## 프림 알고리즘 ##
# 최소 스패닝 트리를 찾는 알고리즘 #
# 크루스칼과 매우 유사. #
# 다만 트리를 만들어나가는 방식이 다름. #
# 크루스칼 -> UNION 느낌이면
# 프림 -> APPEND 느낌
# prim의 시간복잡도는 O(V^2 + E) 밀집 그래프의 경우 V^2와 E의 크기가 유사하기 때문에 #
# 밀집 그래프의 경우 prim 알고리즘 kruskal 알고리즘보다 효율적 #

import heapq


def prim_spanning_tree():
    vector = 7

    graph = [[] for _ in range(vector + 1)]
    graph[1].append((2, 29)); graph[2].append((1, 29)) 
    graph[1].append((5, 75)); graph[5].append((1, 75))
    graph[2].append((3, 35)); graph[3].append((2, 35))
    graph[2].append((6, 34)); graph[6].append((2, 34))
    graph[3].append((4, 7)); graph[4].append((3, 7))
    graph[4].append((6, 23)); graph[6].append((4, 23))
    graph[4].append((7, 13)); graph[7].append((4, 13))
    graph[5].append((6, 53)); graph[6].append((5, 53))
    graph[6].append((7, 25)); graph[7].append((6, 25))

    def prim(graph, vector):
        parent = [0] * (vector + 1)
        for i in range(1, vector+1):
            parent[i] = i
        parent[1] = 1
        pQueue = []
        added = [False] * (vector+1)
        selected_edges = []
        result = 0
        heapq.heappush(pQueue, (0, 1))

        while pQueue:
            weight, here = heapq.heappop(pQueue)
            if added[here] == True:
                continue
            for vertex in graph[here]:
                there = vertex[0]
                cost = vertex[1]
                if not added[there]:
                    heapq.heappush(pQueue, (cost, there))
                    parent[there] = here
            if parent[here] != here:
                selected_edges.append((parent[here], here, weight))
            added[here] = True
            result += weight

        return selected_edges, result

    selected_edges, cost = prim(graph, vector)
    print(selected_edges)
    print(cost)


if __name__ == "__main__":
    prim_spanning_tree()
