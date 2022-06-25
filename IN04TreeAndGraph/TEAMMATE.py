## 팀 결성 ##

# disjoint problem #

import time


def solution():
    def find_parent(parent, a):
        if parent[a] != a:
            parent[a] = find_parent(parent, parent[a])
        return parent[a]

    def union(parent, a, b):
        aP = find_parent(parent, a)
        bP = find_parent(parent, b)
        if aP < bP:
            parent[bP] = aP
        else:
            parent[aP] = bP

    def is_same_team(a, b):
        if find_parent(parent, a) == find_parent(parent, b):
            return True
        else:
            return False

    n, m = map(int, input().split())

    parent = [0] * (n+1)
    for i in range(1, n + 1):
        parent[i] = i

    for i in range(m):
        oper, a, b = map(int, input().split())
        if oper == 0:
            union(parent, a, b)
        elif oper == 1:
            if is_same_team(a, b):
                print("YES")
                continue
            print("NO")


if __name__ == "__main__":
    start = time.time()
    solution()
    print("RUNNING TIME: {}".format(time.time() - start))
