## 크루스칼 알고리즘 ##
# 최소 스패닝 트리의 cost를 찾는 알고리즘 #
# 핵심 아이디어는
# 간선의 가중치가 낮은 순으로 정렬
# 해당 간선들을 집합에 union
# 단 사이클이 생기는 간선의 경우 집합에 union x == find_parent == find_parent 인 경우,,
# 시간복잡도는! 컴포넌트 비교는 간선 수 만큼임. O(E) 하지만
# 정렬이 복잡도를 지배하기 때문에.. 정렬의 시간복잡도 == 크루스칼 시간복잡도

# 루트 노트 탐색
def find_parent(parent, x):
    if parent[x] != x:
        # 루트 노드가 나올때 까지 재귀
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 union
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

vector = 7
parent = [0] * (vector + 1)

# 각 노드의 부모 노드를 자기 자신으로 초기화
for i in range(1, vector+1):
    parent[i] = i

edges = []
# 코스트순으로 오름차순 정렬을 위해..
edges.append((29, 1, 2))
edges.append((75, 1, 5))
edges.append((35, 2, 3))
edges.append((34, 2, 6))
edges.append((7, 3, 4))
edges.append((23, 4, 6))
edges.append((13, 4, 7))
edges.append((53, 5, 6))
edges.append((25, 6, 7))

edges.sort()

selected_edges = []
result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        selected_edges.append(edge)
        result += cost


print(result)
print(selected_edges)
