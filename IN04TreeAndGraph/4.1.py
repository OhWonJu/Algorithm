## 노드 사이의 경로 ##

# 방향 그래프에서 두 노드 사이의 경로가 존재하는지 확인 #

# 경로 탐색은 DFS or BFS #
# 두 방식의 장단점을 이해하고 설명할 수 있어야한다. #

from collections import deque
vector = 5
graph = [
    [],
    [2, 3],
    [4],
    [5],
    [3],
    [],
]
start = 1
end = vector


def dfs_solution():
    # 깊이 우선 탐색
    # 재귀 - BFS 대비 직관적이고 단순
    # 특정 인접 노드를 깊이 탐색할 수 있음
    visited = [False] * (vector + 1)

    def dfs(graph, here, end, visited):
        visited[here] = True
        if visited[end] == True:
            return True
        for there in graph[here]:
            if not visited[there]:
                dfs(graph, here=there, end=end, visited=visited)
        if visited[end] == True:
            return True

    result = dfs(graph, here=start, end=end, visited=visited)
    print(result)
    if result:
        print("Exist")
    else:
        print("Not exist")


def bfs_solution():
    # 너비 우선 탐색
    # 큐를 이용
    # 최단 경로를 찾기데 더 유용함
    visited = [False] * (vector+1)

    def bfs(graph, start, end, visited):
        queue = deque([start])
        visited[start] = True
        while queue:
            here = queue.popleft()
            for there in graph[here]:
                if not visited[there]:
                    if there == end:
                        return True
                    queue.append(there)
                    visited[there] = True
    result = bfs(graph, start=start, end=end, visited=visited)
    if result:
        print("Exist")
    else:
        print("Not exist")


if __name__ == "__main__":
    # dfs_solution()
    bfs_solution()
