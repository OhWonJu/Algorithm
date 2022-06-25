## 위상 정렬 ##

# DFS 기반이 아닌 Queue 자료구조를 이용한 위상정렬 #
# 큐에 들어오고 나가는 순에 따라 위상 정렬이 이루어짐 #
# 큐에 먼저 들어오고 먼저 나갈수록 진입차수가 낮은 원소였던 것. #
# 사이클 발생시 위상 정렬은 모든 벡터를 방문하기전에 종료되야함. #
# 위상 정렬 문제 대부분은 사이클을 배제한 형태이기 때문에 일단 패쓰 #

from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    indegree[v] += 1


def topology_sort():
    result = []
    q = deque()

    # 최초 진입차수가 0인 원소를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때 까지.
    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 모든 간선을 끊는다.
        for there in graph[now]:
            indegree[there] -= 1
            if indegree[there] == 0:
                q.append(there)

    print(result)


topology_sort()
