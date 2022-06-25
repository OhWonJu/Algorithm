## 도시 분할 계획 ##
# 집합 내의 최소개의 edge, weight #
# 2개의 최소 스패닝 트리 #
# 1개의 최소 스패닝 트리를 구한 뒤 weight가 가장 큰 간선을 지우면...분리..! #

## 최소 스패닝 트리 ==> 모든 원소를 방문(v-1개의 edge사용) 단 total weight가 최소가 되게. ##
# 여기서 여러개의 스패닝 트리로 분할 하고 싶음 -> 구해진 단일 스패닝 트리를 원하는 조건에 따라 분할 #

import time


def solution():
    n, m = map(int, input().split())

    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))

    def kruskal(n, edges):
        edges.sort()
        parent = [0] * (n+1)
        for i in range(1, n+1):
            parent[i] = i

        result = 0
        weigthest = 0

        def find_parent(parent, x):
            if parent[x] != x:
                parent[x] = find_parent(parent, parent[x])
            return parent[x]

        def union(parent, a, b):
            aP = find_parent(parent, a)
            bP = find_parent(parent, b)
            if aP < bP:
                parent[bP] = aP
            else:
                parent[aP] = bP

        for cost, here, there in edges:
            if find_parent(parent, here) != find_parent(parent, there):
                union(parent, here, there)
                result += cost
                weigthest = max(weigthest, cost)
        return result - weigthest

    result = kruskal(n, edges)
    print(result)


if __name__ == "__main__":
    solution()
