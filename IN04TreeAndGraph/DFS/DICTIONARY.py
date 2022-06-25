## 고대어 사전 ##

## DFS 위상정렬 ##

import time
from collections import deque


def Test():
    words = ["dictionary", "english", "is", "ordered", "ordinary", "this"]

    # 알파벳 기준이니까 그래프 표현의 범위가 크지 않음. 26 X 26
    # 인접 행렬 낫벧?
    graph = [
        ([0] * 26) for _ in range(26)
    ]

    def Make_Graph(words):
        # 전체 문자열 수 만큼
        for j in range(1, len(words)):
            # 인접한 두 단어쌍만 검사...위상정렬에 필요한 모든 정보를 얻을 수 있을까? YES...
            i = j - 1
            # 두 문자열 중 짧은 것 기준 반복
            length = min(len(words[i]), len(words[j]))
            for k in range(length):
                # 이전 문자열의 특정 문자가 빠르다면 방향 그래프 간선 생성
                if(words[i][k] != words[j][k]):  # 앞 단어가 뒤 단어의 접두사인 경우도 예외처리 해줌
                    a = ord(words[i][k]) - ord('a')
                    b = ord(words[j][k]) - ord('a')
                    graph[a][b] = 1
                    break

    order = deque()
    visited = []

    def DFS(prev, here):
        visited[here] = True
        haveEdge = False
        for e in graph[here]:
            # 간선이 있냐 없냐
            if(e != 0):
                haveEdge = True
                break
        if(not haveEdge and prev == None):
            order.append(here)
            return

        for there in range(len(graph[here])):
            if(graph[here][there] != 0 and not visited[there]):
                DFS(here, there)
        order.appendleft(here)

    # 위상정렬 #
    # 들어오는 간선이 하나도 없는 경우 정렬 결과의 뒤에 붙인다.
    # 그래프에서 이 정점을 지운다.
    # 반복
    def Topological_Sort():
        m = len(graph)
        nonlocal visited
        visited = [False] * m
        order.clear()
        for i in range(m):
            if(not visited[i]):
                DFS(None, i)
        for i in range(m):
            for j in range(i+1, m):
                if graph[order[j]][order[i]]:
                    return
        return order

    Make_Graph(words)
    result = Topological_Sort()

    if(result == None):
        print("INVALID HYPOTHESIS")
    else:
        def typeChager(c):
            return chr(c + 97)
        c = list(map(typeChager, result))
        print(c)


def Solution():
    pass


if __name__ == "__main__":
    start = time.time()

    Test()

    print("RUNNING TIME: {}".format(time.time()-start))
