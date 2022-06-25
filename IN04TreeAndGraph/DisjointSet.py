## 서로소 집합 자료구조 구현 ##

# 부모를 거슬러 올라 루트를 찾는다.
def find_parent(parent, x):
    # 부모 테이블에 자기자신이 부모이면 root
    if (parent[x] != x):
        # 경로 압축
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소의 집합을 union
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if(a < b):
        parent[b] = a
    else:
        parent[a] = b


if __name__ == "__main__":
    v, e = map(int, input().split())
    parent = [0] * (v+1)  # 0번 인덱스 넘겨서 표현한듯

    for i in range(1, v+1):
        parent[i] = i

    for i in range(e):
        a, b = map(int, input().split())
        union_parent(parent, a, b)

    print("각 원소가 속한 집합: ", end="")
    for i in range(1, v+1):
        print(find_parent(parent, i), end=" ")

    print()

    print("부모 테이블: ", end="")
    for i in range(1, v+1):
        print(parent[i], end=" ")
