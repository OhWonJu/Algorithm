## Bellman Ford 최단거리 알고리즘 ##
# 음수 사이클에 대한 판별이 가능함. #
# upper에 대한 갱신을 통한 판별.... V 번 반복하여 V번째에 완화가 있다면... 음수 사이클 #
# 음수 사이클이 없다면 V-1번째에 모든 완화가 이루어짐.. V부터는 완화 없음 #

INF = int(1e9)

start = 1
node = 5
#edge = 6

graph = [[] for _ in range(node + 1)]

graph[1].append((2, 4))
graph[1].append((3, 4))
graph[3].append((4, -2))
graph[4].append((3, 5))
graph[5].append((2, -4))
graph[5].append((5, -1))


def bellman_Ford(start):
    upper = [INF] * (node + 1)
    upper[start] = 0

    updated = None

    for _ in range(node):
        updated = False
        for here in range(1, node+1):
            for there, cost in graph[here]:
                if upper[there] > upper[here] + cost:
                    upper[there] = upper[here] + cost
                    updated = True
        if(not updated):
            break
    if(updated):
        upper.clear()
    return upper

result = bellman_Ford(start)
print(result)