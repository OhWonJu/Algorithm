# 합의 경로
# 득정 합이 되는 경로의 수를 카운팅
# 부모노드에서 자식노드로 밖에 이동 불가.


from Tree import BinaryNode as Node

root = Node(10)
l1 = Node(5, parent=root)
l2 = Node(3, parent=l1)
l3 = Node(1, parent=l1)
l4 = Node(3, parent=l2)
l5 = Node(-2, parent=l2)
l6 = Node(2, parent=l3)

r1 = Node(-3, parent=root)
r2 = Node(11, parent=r1)


def solution1():
    # 무식한 방법
    # 가능한 모든 경로를 다 파악 (트리의 모든 경로 훑기)
    # 원하는 값을 가지는 경로의 수를 센다.

    # 현재 노드에서 시작해서 합의 조건을 만족하는 경로의 수를 반환
    def count_path_with_sum_from_node(node, targetSum, currentSum):
        if node == None:
            return 0
        currentSum += node.data
        totalPaths = 0
        if currentSum == targetSum:
            totalPaths += 1
        totalPaths += count_path_with_sum_from_node(
            node.left, targetSum, currentSum)
        totalPaths += count_path_with_sum_from_node(
            node.right, targetSum, currentSum)
        return totalPaths

    # 재귀적으로 내려가면서 모든 경로를 훑는다.
    def count_path_with_sum(root, targetSum):
        if root == None:
            return 0
        # 루트로부터 시작
        pathsFromRoot = count_path_with_sum_from_node(root, targetSum, 0)
        # 루트의 왼쪽 자식 노드로부터 시작
        pathsOnLeft = count_path_with_sum(
            root.left, targetSum)
        # 루트의 오른쪽 자식 노드로부터 시작
        pathsOnRight = count_path_with_sum(
            root.right, targetSum)
        return pathsFromRoot + pathsOnLeft + pathsOnRight

    paths = count_path_with_sum(root, 8)
    print(paths)
    # 깊이가 d에 놓인 노드는 총 d번 방문
    # 균형 이진 트리에서는 logN 깊이
    # 전체 노드 N개에 대해 logN번의 호출이 발생하니
    # 시간복잡도는 따라서 O(NlogN)
    # 하지만 Skewed Tree와 같이 균형 이진 트리가 아니라면....🤦🏻‍♂️

# 최적화가 필요하다..!
# 반복적으로 지나가는 path들을 처리하면 좋을텐데..
# 현재 까지 쌓인 값 - 목표 값 = 만족하는 경로의 개수...running Sums....


def solution2():
    # running sum 개념....
    # running sum -> s에서 지금 위치까지의 합
    # s -> y 의 값에서
    # s -> x 의 값을 뻇을 때
    # 원하는 값이면 y에서 x전까지 경로가 원하는 경로!

    # runningSum - targetSum 값을 해시테이블에서 찾기
    # runningSum = targetSum 루트에서 시작하는 경로가 원하는 값
    # DFS 기반으로 해당 알고리즘 구현

    hashMap = {}

    def path_count(pathSum, hashMap):
        count = 0
        if pathSum in hashMap:
            count = hashMap[pathSum]
        return count

    def increment_hash_map(hashMap, key, delta):
        newCount = path_count(key, hashMap) + delta
        if newCount == 0:
            # 공간 절약을 위해 값이 0이 되면 제거한다
            del hashMap[key]
        else:
            hashMap[key] = newCount

    def count_paths_with_sum(node, targetSum, runningSum, hashMap):
        # 기저 조건
        if node == None:
            return 0
        # 현재 노드에서 끝나면서 합의 조건을 만족하는 경로의 수
        runningSum += node.data
        pathSum = runningSum - targetSum
        totalPath = path_count(pathSum, hashMap)
        # 루트로부터~ 인 경우
        if runningSum == targetSum:
            totalPath += 1
        # pathCount를 증가시키고, recusion call 한 뒤, pathCount를 감소
        # 해당 runningSum이 있다고 표시하고,, 자기로 돌아왔을 때 표시를 지운다는 느낌
        increment_hash_map(hashMap, runningSum, 1)
        totalPath += count_paths_with_sum(node.left,
                                          targetSum, runningSum, hashMap)
        totalPath += count_paths_with_sum(node.right,
                                          targetSum, runningSum, hashMap)
        increment_hash_map(hashMap, runningSum, -1)

        return totalPath

    def call_count_paths(root, targetSum):
        return count_paths_with_sum(root, targetSum, 0, hashMap)

    result = call_count_paths(root, 8)
    print(result)


if __name__ == "__main__":
    # solution1()
    solution2()
