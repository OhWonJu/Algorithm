## 순서 정하기 ##
# 위상 정렬 문제
# Topological Sort #

# Topological Sort 혹은 DFS로 해결 가능

from collections import deque


def solution():
    p = input().split()
    dependence = {}
    indegree = {}
    for key in p:
        dependence[key] = []
        indegree[key] = 0
    edges = 0
    while True:
        try:
            dom, sub = input().split()
        except ValueError:
            break
        dependence[dom].append(sub)
        indegree[sub] += 1
        edges += 1


    def topological_sort():
        result = []
        queue = deque()
        for key, value in indegree.items():
            if value == 0:
                queue.append(key)
        while queue:
            here = queue.popleft()
            result.append(here)
            for edge in dependence[here]:
                indegree[edge] -= 1
                if indegree[edge] == 0:
                    queue.append(edge)
        return result

    result = topological_sort()
    print(result)


if __name__ == "__main__":
    solution()
