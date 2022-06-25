## 미해결.. 뭐야 이거.. ##
## BST 수열 ##
# 특정 BST가 주어졌을 때. (중복이 없다는 가정)
# 해당 BST를 만들 수 있는 수열의 집합(배열)을 출력하면 됩니다.
# 배열의 왼쪽부터 들어간다고 가정

# 루트는 배열의 첫 원소이어야 한다.
# 재귀적으로 수열 케이스를 만들어서 합치면 되지 않나?

from Tree import BinarySearchNode as Node
from collections import deque
import copy

root = Node(2)
a0 = Node(1, parent=root)

b0 = Node(3, parent=root)


def solution():
    def weave_list(first, second, results, prefix):
        # 모든 수열을 엮음
        # 각 재귀마다 left, right 중 하나의 첫 원소를 제거하는 방식

        # 리스트 하나가 비었을 때 나머지 리스트를 *copy된 prefix에 추가한 뒤 결과를 저장
        if len(first) == 0 or len(second) == 0:
            # 파이썬에서 리스트의 원소가 바뀌는 경우 새 리스트를 파는 shallow copy가 기본..
            result = prefix
            result.append(*first) if len(first) != 0 else None
            result.append(*second) if len(second) != 0 else None
            results.append(result)
            return
        # first의 첫 원소를 prefix로 옮긴 뒤 재귀
        # 호출이 끝난 뒤에는 원상 복구
        headFirst = first.popleft()
        prefix.append(headFirst)
        weave_list(first, second, results, prefix)
        prefix.pop()
        first.appendleft(headFirst)

        headSecond = second.popleft()
        prefix.append(headSecond)
        weave_list(first, second, results, prefix)
        prefix.pop()
        second.appendleft(headSecond)

    def all_sequences(node):
        result = deque()
        if node == None:
            result.append([])
            return result
        prefix = []
        prefix.append(node.data)

        # 왼쪽, 오른쪽 부분 트리에 대한 재귀
        leftSeq = all_sequences(node.left)
        rightSeq = all_sequences(node.right)

        # 두 결과 리스트를 하나로 엮음
        for left in leftSeq:
            for right in rightSeq:
                weaved = deque()
                weave_list(left, right, weaved, prefix)
                result.append(weaved)
        return result

    result = list(all_sequences(root))
    print(result)


if __name__ == "__main__":
    solution()
