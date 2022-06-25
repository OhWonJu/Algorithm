## 변화하는 중간 값 ##

# 주어진 수열을 정렬하여 양분한다.
# 앞 절반을 최대 힙, 뒤 절반을 최소 힙
# 최대 힙의 root가 중간 값이 된다.

# 삽입 불변식
# 1. 최대힙의 크기는 최소힙의 크기와 같거나, 하나 더 크다
# 2. 최대 힙의 최대 원소는 최소힙의 최소 원소보다 작거나 같다.

import heapq


def Solution():
    class RNG:
        def __init__(self, a=None, b=None):
            self.seed = 1983
            self.a = a
            self.b = b

        def next(self):
            ret = self.seed
            self.seed = ((self.seed * self.a) + self.b) % 20090711
            return ret

    def runningMedian(n, rng):
        maxHeap = []
        minHeap = []
        maxLen = minLen = 0
        ret = 0
        # 반복 불변식
        for cnt in range(1, n+1):
            # 1. 최대힙의 크기는 최소힙의 크기와 같거나, 하나 더 크다
            if(maxLen == minLen):
                seed = rng.next()
                heapq.heappush(maxHeap, (-seed, seed))
                maxLen += 1
            else:
                heapq.heappush(minHeap, rng.next())
                minLen += 1
            # 2번 불변식이 깨졌을 경우 복구
            if(minLen != 0 and maxLen != 0 and minHeap[0] < maxHeap[0][1]):
                a = maxHeap[0], b = minHeap[0]
                heapq.heappop(maxHeap), heapq.heappop(minHeap)
                heapq.heappush(maxHeap, (-b, b))
                heapq.heappush(minHeap, a)
            ret = (ret + maxHeap[0][1]) % 20090711
        return ret

    ret = runningMedian(10, RNG(1, 0))
    print(ret)

if __name__ == "__main__":
    Solution()
