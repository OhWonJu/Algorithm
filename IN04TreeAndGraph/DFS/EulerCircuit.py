## Euler circuit ##

# 오일러 서킷의 조건
# 1. 컴포넌트가 하나여야...?  =  DFS실행 이후 모든 간선을 통과했는지 확인 가능
# -> 단 나머지 컴포넌트에 에지가 없으면 ㄱㅊ.. = 모두 통과했다면 컴포넌트가 있던지 없던지 상관 없음
# 2. 그래프의 모든 정점들의 차수가 짝수이어야 오일러 서킷이 존재할 수 있다.

# 유향 그래프의 경우..
# - in-degree와 out-degree가 같아야 함.
# 무향 그래프의 경우..
# - just 짝수의 차수 = DFS를 돌고 남는 간선이 없으면 circuit!

from collections import deque
from typing import Text


def Non_Directional():
    graph = [
        ([0] * 7) for _ in range(7)
    ]
    graph[0][1] = graph[1][0] = 1
    graph[0][2] = graph[2][0] = 1
    graph[1][4] = graph[4][1] = 1
    graph[2][3] = graph[3][2] = 1
    graph[3][4] = graph[4][3] = 1
    graph[4][5] = graph[5][4] = 1
    graph[4][6] = graph[6][4] = 1
    graph[5][6] = graph[6][5] = 1

    circuit = deque()

    def Get_EulerCircuit(here, graph):
        for there in range(len(graph[here])):
            while(graph[here][there] > 0):
                graph[here][there] -= 1
                graph[there][here] -= 1
                Get_EulerCircuit(there, graph)
        circuit.appendleft(here)

    def Check_Condition(graph):
        for row in graph:
            edges = 0
            for col in row:
                edges += col
            if (edges % 2 != 0):
                return False
        return True

    if(Check_Condition(graph)):
        Get_EulerCircuit(0, graph)
        print(circuit)
    else:
        print("This Graph is not EulerCircuit.")


def Directional():
    graph = [
        ([0] * 7) for _ in range(7)
    ]
    graph[0][1] = 1
    graph[1][4] = 1
    graph[4][3] = 1
    graph[4][5] = 1
    graph[5][6] = 1
    graph[6][4] = 1
    graph[3][2] = 1
    graph[2][0] = 1

    #graph[0][1] = 1
    #graph[1][2] = 1
    #graph[2][3] = 1
    #graph[3][0] = 1
    #graph[4][5] = 1
    #graph[5][4] = 1

    inDegree = [0] * len(graph)
    outDegree = [0] * len(graph)

    totalEdges = 0

    circut = deque()

    def Get_Degrees(graph):
        nonlocal totalEdges
        totalEdges = 0
        for here in range(len(graph)):
            for there in range(len(graph[here])):
                outDegree[here] += graph[here][there]
                inDegree[here] += graph[there][here]
                totalEdges += graph[here][there]

    def Check_Condition():
        for i in range(len(graph)):
            if(inDegree[i] != outDegree[i]):
                return False
        return True

    def Get_EulerCircuit(here, graph):
        nonlocal totalEdges
        for there in range(len(graph[here])):
            while(graph[here][there] > 0):
                graph[here][there] -= 1
                totalEdges -= 1
                Get_EulerCircuit(there, graph)
        circut.appendleft(here)

    Get_Degrees(graph)

    if(Check_Condition()):
        Get_EulerCircuit(0, graph)
        if(totalEdges != 0):
            print("This Graph is not EulerCircuit.")
        else:
            print(circut)
    else:
        print("This Graph is not EulerCircuit.")


if __name__ == "__main__":
    # Non_Directional()
    Directional()


# 참고
# https://sonsh0824.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B3%B5%EB%B6%804-%ED%95%9C%EB%B6%93%EA%B7%B8%EB%A6%AC%EA%B8%B0Eulerian-circuit
# https://hy38.github.io/euilerian-circuit-and-trail
