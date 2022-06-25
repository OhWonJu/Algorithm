## 오일러 트레일 ##

# 서킷과 유사하지만 시작점 v와 끝점 u가 다른 경우임
# v != u
# v와 u는 홀수의 edge를 가져야함

# 무향 오일러 트레일
# - v와 u의 차수가 홀수
# - 나머지 vector의 edge는 짝수

# 유향 오일러 트레일
# - v는 최종적으로 나가야 하기 떄문에 indegree + 1 = outdegree
# - u는 반대로 최종적으로 들어와야함. outdegree + 1 = indegree
# - 나머지 vector의 경우 indegree == outdegree

# 트레일 구현
# v와 u를 잇는 edge를 추가하여 오일러 서킷을 만듦
# 생성한 edge를 제거
# 재귀에서 circuit을 최초로 기록하는 시점은 마지막 정점에서 최초 정점으로 돌아온 경우임
# 트레일은 최초 기록을 지우기만 하면 됨.

from collections import deque


def Non_Directional():
    graph = [
        ([0] * 7) for _ in range(7)
    ]
    graph[0][1] = graph[1][0] = 1
    #graph[0][2] = graph[2][0] = 1
    graph[1][4] = graph[4][1] = 1
    graph[2][3] = graph[3][2] = 1
    graph[3][4] = graph[4][3] = 1
    graph[4][5] = graph[5][4] = 1
    graph[4][6] = graph[6][4] = 1
    graph[5][6] = graph[6][5] = 1

    totalEdges = 0
    trailPoints = []
    circuit = deque()

    def Get_EulerTrail(here, graph):
        nonlocal totalEdges
        for there in range(len(graph[here])):
            while(graph[here][there] > 0):
                graph[here][there] -= 1
                graph[there][here] -= 1
                totalEdges -= 1
                Get_EulerTrail(there, graph)
        circuit.appendleft(here)

    def Check_Condition(graph):
        nonlocal totalEdges
        totalEdges = 0
        for row in range(len(graph)):
            edges = 0
            for col in graph[row]:
                totalEdges += col
                edges += col
            if (edges % 2 != 0):
                trailPoints.append(row)
        totalEdges /= 2
        if(len(trailPoints) == 2):
            return True
        else:
            return False

    if(Check_Condition(graph)):
        graph[trailPoints[0]][trailPoints[1]] += 1
        graph[trailPoints[1]][trailPoints[0]] += 1
        totalEdges += 1
        Get_EulerTrail(trailPoints[0], graph)
        graph[trailPoints[0]][trailPoints[1]] -= 1
        graph[trailPoints[1]][trailPoints[0]] -= 1
        if(totalEdges != 0):
            print("This Graph is not Euler Trail.")
        else:
            circuit.pop()
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
    graph[4][6] = 1
    graph[6][5] = 1
    graph[5][4] = 1
    graph[3][2] = 1

    #graph[0][1] = 1
    #graph[1][2] = 1
    #graph[2][3] = 1
    #graph[3][0] = 1
    #graph[4][5] = 1
    #graph[5][4] = 1

    inDegree = [0] * len(graph)
    outDegree = [0] * len(graph)

    totalEdges = 0
    startPoint = endPoint = None
    circuit = deque()

    def Get_Degrees(graph):
        nonlocal totalEdges
        totalEdges = 0
        for here in range(len(graph)):
            for there in range(len(graph[here])):
                outDegree[here] += graph[here][there]
                inDegree[here] += graph[there][here]
                totalEdges += graph[here][there]

    def Check_Condition():
        nonlocal startPoint
        nonlocal endPoint
        for i in range(len(graph)):
            if(inDegree[i] != outDegree[i]):
                if((inDegree[i] + 1 == outDegree[i]) and startPoint == None):
                    startPoint = i
                elif((inDegree[i] == outDegree[i] + 1) and endPoint == None):
                    endPoint = i
                else:
                    return False
        return True

    def Get_EulerTrail(here, graph):
        nonlocal totalEdges
        for there in range(len(graph[here])):
            while(graph[here][there] > 0):
                graph[here][there] -= 1
                totalEdges -= 1
                Get_EulerTrail(there, graph)
        circuit.appendleft(here)

    Get_Degrees(graph)

    if(Check_Condition()):
        graph[endPoint][startPoint] += 1
        totalEdges += 1
        Get_EulerTrail(startPoint, graph)
        graph[endPoint][startPoint] -= 1
        if(totalEdges != 0):
            print("This Graph is not EulerCircuit.")
        else:
            circuit.pop()
            print(circuit)
    else:
        print("This Graph is not EulerCircuit.")


if __name__ == "__main__":
    #Non_Directional()
    Directional()