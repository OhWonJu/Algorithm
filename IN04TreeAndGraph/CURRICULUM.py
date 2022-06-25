## Topological Problem ##
# 위상 정렬이니까 queue 사용해보자. #

from collections import deque
import copy

def solution():
    n = int(input())

    indegree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    times = [0] * (n+1)  # 각 강의 수강 시간

    for i in range(1, n+1):
        inputs = list(map(int, input().split()))
        times[i] = inputs[0]
        for x in inputs[1:]:
            if x == -1:
                break
            indegree[i] += 1
            graph[x].append(i)

    def topology_sort():
        result = copy.deepcopy(times)
        q = deque()

        for i in range(1, n+1):
            if indegree[i] == 0:
                q.append(i)

        while q:
            now = q.popleft()
            for there in graph[now]: # 햔재 노드에서 향하는 edge에 대하야
                indegree[there] -= 1 # there의 진입차수 감소
                result[there] = max(result[there], result[now] + times[there])
                if indegree[there] == 0:
                    q.append(there)
        for i in range(1, n+1):
            print(result[i])

    topology_sort()


if __name__ == "__main__":
    solution()
