## Depth-First-Search ##

# 그래프 표현
# 1. adjacency Matrix
# 2. adjacency List

INF = 99999999

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)

# 파이썬에서의 인접리스트... list 자료형이 배열, 리스트 다 커버
graph = [[] for _ in range(3)]
graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)

# DFS는 Stack에 기초하여 작동
# DFS는 recursion으로 구현

def DFS(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if(not visited[i]):
            DFS(graph, i, visited)

# DFS는 그래프 표현 방식에 따라 시간 복잡도가 달라짐. 당연한거 아녀?
# 인접 리스트 O(V + E)
# 인접 행렬 O(V^2)

# 이거 인접리스트구나..
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

visited = [False] * 8
DFS(graph, 0, visited)
print()

# DFS 활용
# 두 정점의 연결 여부
# 컴포넌트 수 파악
# 위상 정렬