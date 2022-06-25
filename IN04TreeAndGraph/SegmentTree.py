import math
from multipledispatch import dispatch

## 구간 최소 트리 Range Minimum Query ##


class RMQ:
    def __init__(self, array=None):
        self.n = len(array)
        # 2^(log(n)+1)-1  구간 트리 초기화
        # 구간 트리는 full binary Tree의 성질을 가지고 있다.
        self.rangeMin = [None]*(pow(2, math.ceil(math.log(self.n, 2))+1)-1)
        self.init(array, node=0, left=0, right=self.n-1)

    # init의 시간 복잡도는 전체 node수에 비례한다.. O(N)
    def init(self, array, node, left, right):
        if(left == right):
            self.rangeMin[node] = array[left]
            return self.rangeMin[node]
        mid = (left + right) // 2
        leftMin = self.init(array, node*2+1, left, mid)
        rightMin = self.init(array, node*2+2, mid+1, right)
        self.rangeMin[node] = min(leftMin, rightMin)
        return self.rangeMin[node]

    @dispatch(int, int, int, int, int)
    def query(self, left, right, node, nodeLeft, nodeRight):
        # 두 구간이 겹치지 않는 경우. (공집합)
        if(left > nodeRight or right < nodeLeft):
            return None
        # Node의 표현 범위가 array[left, right] 범위에 완전히 포함되는 경우
        if(left <= nodeLeft and nodeRight <= right):
            return self.rangeMin[node]
        mid = (nodeLeft + nodeRight) // 2
        leftResult = self.query(left, right, node*2+1, nodeLeft, mid)
        rightResult = self.query(left, right, node*2+2, mid+1, nodeRight)
        if (leftResult == None and rightResult == None): return None
        elif(leftResult == None):
            return rightResult
        elif(rightResult == None):
            return leftResult
        return min(leftResult, rightResult)

    @dispatch(int, int)
    def query(self, left, right):
        return self.query(left, right, 0, 0, self.n-1)

    @dispatch(int, int, int, int, int)
    def update(self, index, newValue, node, nodeLeft, nodeRight):
        if(index < nodeLeft or nodeRight < index):
            return self.rangeMin[node]
        if(nodeLeft == nodeRight):
            self.rangeMin[node] = newValue
            return self.rangeMin[node]

        mid = (nodeLeft + nodeRight) // 2
        self.rangeMin[node] = min(self.update(index, newValue, node*2+1, nodeLeft, mid),
                                  self.update(index, newValue, node*2+2, mid+1, nodeRight))
        return self.rangeMin[node]

    @dispatch(int, int)
    def update(self, index, newValue):
        return self.update(index, newValue, 0, 0, self.n-1)


if __name__ == "__main__":
    l = [2, 1, 5, 7, 8, 1, 0, 16, 6, 9, 7, 3, 6, 5, 12]
    rmq = RMQ(l)
    print(rmq.query(7, 14))
    rmq.update(3, 1)
    print(rmq.query(2,4))

    
