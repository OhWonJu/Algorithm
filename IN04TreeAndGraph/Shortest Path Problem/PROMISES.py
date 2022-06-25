import time
import sys
input = sys.stdin.readline

## 플로이드 워셜 변형 ##
# 기존 플로이드 워셜은 vector 집합의 증가임 #
# 해당 변형은 경유하는 vector의 목록을 늘리는 대신 #
# 경유하는 edge의 목록을 늘리는 방식 #
# O(v^3) 이 아닌 O(V^2) 만으로 플로이드 워셜 수행.. #

### 핵심은 새 간선이 그래프에 추가되었을 때 최단 거리 갱신 ###
## 굳이 정점간의 비교를 할 필요가 없다는 것! ##

def solution():
    INF = int(1e9)

    case = int(input())
    result = [0] * case

    def update(u, v, w, c):
        nonlocal graph
        if(graph[u][v] <= w):
            return False
        # O(V^2) 
        for start in range(1, c+1):
            for end in range(1, c+1):
                graph[start][end] = min(graph[start][end], min(
                    graph[start][u] + w + graph[v][end], graph[start][v] + w + graph[u][end]))
        return True

    for i in range(case):
        city, exist, future = map(int, input().split())
        graph = [[INF] * (city + 1) for _ in range(city + 1)]

        for here in range(1, city + 1):
            for there in range(1, city + 1):
                if here == there:
                    graph[here][there] = 0
                    
        for _ in range(exist):
            u, v, w = map(int, input().split())
            graph[u][v] = graph[v][u] = w

        for _ in range(future): # V^2N
            u, v, w = map(int, input().split())
            if(not update(u, v, w, city)):
                result[i] += 1

    for r in result:
        print(r)


if __name__ == "__main__":
    start = time.time()
    solution()
    print("RUNNING TIME {}".format(time.time() - start))
