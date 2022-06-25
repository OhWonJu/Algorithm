## Breadth First Search ##

# BFS는 queue 자료구조를 통해 구현

from collections import deque


def BFS(graph, start, discovered):
    queue = deque([start])
    discovered[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if(not discovered[i]):
                queue.append(i)
                discovered[i] = True


graph = [
    [1, 2, 7],
    [0, 6],
    [0, 3, 4],
    [2, 4],
    [2, 3],
    [6],
    [1, 5, 7],
    [0, 6]
]

discovered = [False] * 8
BFS(graph, 0, discovered)
print()

# DFS에 반해 BFS는 shortest path문제에만 사용..
# BFS -> 너비우선탐색 스패닝 트리가 생성됨. 시작점에서 부터 다른 정점까지의 최소 거리를 알 수 있게 됨
# 최소 스패닝 트리의 기본 개념!
