# 너비 우선 탐색은 최단 경로 문제에 대해서만 사용됨.. #

# 덱에 저장되는 형태 때문에 이게 가능한듯
# 발견 시점에 따라 저장되는 타임이 다르고 이게 꼬일 수 없으니까.
# ==> 너비 우선 탐색 스패닝 트리가 생성되고...이 트리에서 각 노드간의 최단 거리를 찾을 수 있음..

from collections import deque


def Solution():
    graph = [
        [1, 3, 4],
        [0, 2, 3],
        [1, 5, 6],
        [0, 1, 6],
        [0, 5],
        [2, 4],
        [2, 3, 8],
        [0],
        [6]
    ]

    distance = None
    parent = None

    def BFS(graph, start):
        nonlocal distance
        nonlocal parent
        distance = [-1] * len(graph)  # 시작점과의 거리
        parent = [-1] * len(graph)  # 해당 노드의 부모 노드
        queue = deque([start])
        distance[start] = 0
        parent[start] = start

        while queue:
            here = queue.popleft()
            for there in graph[here]:
                if(distance[there] == -1):
                    queue.append(there)
                    distance[there] = distance[here] + 1
                    parent[there] = here

    def shortest_Path(v, parent):
        path = deque([v])
        while True:
            v = parent[v]
            path.appendleft(v)
            if(parent[v] == v):
                break
        return path

    BFS(graph, 0)
    print(shortest_Path(8, parent))


if __name__ == "__main__":
    Solution()
