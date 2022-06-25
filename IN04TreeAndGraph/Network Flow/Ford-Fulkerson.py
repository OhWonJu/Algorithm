## Ford-Fulkerson flow network algorithm ##

# flow network의 필수 조건
# 1. 용량 제한 속성: 유량은 해당 간선의 용량을 초과할 수 없음
# 2. 유량 대칭성: u -> v 의 유량 만큼 v - u로 음수의 유량이 발생한다고 봄
# 3. 유랑 보존: 소스에서 나간 유량 == 싱크로 들어오는 유량

# 포드-풀커슨 알고리즘
# 유량 넷의 모든 간선의 유량을 0으로 두고 시작, BFS와 유사한 방식으로
# 추가 유량을 보낼 수 있는 경로를 반복해서 찾는 것. = 잔여 용량이 남은 간선들만을 사용하는 BFS을 이용해 aug path를 찾음
# 추가 유량을 보낼 수 없을 때 알고리즘은 종료됨.  거대한 내부 무한반복문 존제..

# 간선의 용량 - 유량 = residual capacity
# augmenting path를 통해 흘려보낼 수 있는 최대 유량 == 포함된 간선 중 잔여 용량이 가장 작은 값

from collections import deque
from flow_edge import Edge as edge


def ford_fulkerson_flow_net():
    INF = int(1e9)
    vector = 6
    graph = [[] for _ in range(vector)]

    graph[0].append(edge(fromVec=0, toVec=1, capacity=16))
    graph[0].append(edge(fromVec=0, toVec=2, capacity=3))
    graph[1].append(edge(fromVec=1, toVec=2, capacity=1))
    graph[1].append(edge(fromVec=1, toVec=3, capacity=20))
    graph[2].append(edge(fromVec=2, toVec=3, capacity=7))
    graph[2].append(edge(fromVec=2, toVec=4, capacity=7))
    graph[3].append(edge(fromVec=3, toVec=2, capacity=5))
    graph[3].append(edge(fromVec=3, toVec=5, capacity=10))
    graph[4].append(edge(fromVec=4, toVec=5, capacity=8))
    

    # for i in range(vector):
    #  for e in graph[i]:
    #    e.print_edge()

    capacitys = [[0] * vector for _ in range(vector)]
    for i in range(vector):
        for e in graph[i]:
            capacitys[e.fromVec][e.toVec] = e.get_capacity()

    flows = [[0] * vector for _ in range(vector)]
    total_flow = 0

    def network_flow(source, sink):
        total_flow = 0
        while True:  # 모든 aug path에 대해 반복한다.
            # 탐색을 위한 초기화
            parent = [-1] * vector
            parent[source] = source
            # BFS
            queue = deque([source])
            while queue and parent[sink] == -1:
                here = queue.popleft()
                for e in graph[here]:
                    # 용량 제한 속성
                    if e.get_capacity() - flows[e.fromVec][e.toVec] > 0 and parent[e.toVec] == -1:
                        queue.append(e.toVec)
                        # 증가 경로를 parent로 표현하며 저장함
                        parent[e.toVec] = e.fromVec
            # 증가경로를 찾지 못한 경우 aug path search 반복을 끝냄
            if parent[sink] == -1:
                break
            # 증가 경로 상의 최소 잔여 용량 탐색
            amount = INF
            p = sink
            while p != source:
                amount = min(capacitys[parent[p]][p] -
                              flows[parent[p]][p], amount)
                p = parent[p]
            # flow 업데이트    
            p = sink
            while p != source:
                # 대칭성 유지를 위해
                flows[parent[p]][p] += amount
                flows[p][parent[p]] -= amount
                for e in graph[parent[p]]:
                    if e.toVec == p:
                        e.add_flow(amount)
                p = parent[p]
            total_flow += amount
        return total_flow

    total_flow = network_flow(0, 5)

    for i in range(vector):
        for e in graph[i]:
            e.print_edge()

    print("Total flow:", total_flow)


if __name__ == "__main__":
    ford_fulkerson_flow_net()
