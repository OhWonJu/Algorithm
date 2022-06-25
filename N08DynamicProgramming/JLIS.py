# 합친 LIS

from bisect import bisect_left


def solution():
    A = [1, 9, 4]
    B = [3, 4, 7]
    cache = []

    def JLIS(idxA, idxB):
        if idxA >= len(A) and idxB >= len(B):
            return
        # 두 배열에서 작은 값을 선택한다.
        el = None
        if idxB >= len(B) or A[idxA] < B[idxB]:
            el = A[idxA]
            idxA += 1
        elif idxA >= len(A) or A[idxA] > B[idxB]:
            el = B[idxB]
            idxB += 1
        else:
            return
        # cache가 비어있거나 선택된 원소가 cache의 마지막원소보다 클경우
        if len(cache) == 0 or cache[-1] < el:
            cache.append(el)
        # cache의 특정원소가 el보다 작은 경우
        else:
            idx = bisect_left(cache, el)
            cache[idx] = el
        JLIS(idxA, idxB)

    JLIS(0, 0)
    print(cache)
    print(len(cache))


def solution2():
    A = [1, 9, 4]
    B = [3, 4, 7]
    cache = []

    idxA = idxB = 0
    while idxA < len(A) or idxB < len(B):
        el = None
        if idxB >= len(B) or A[idxA] < B[idxB]:
            el = A[idxA]
            idxA += 1
        elif idxA >= len(A) or A[idxA] > B[idxB]:
            el = B[idxB]
            idxB += 1
        else:
            continue
        if len(cache) == 0 or cache[-1] < el:
            cache.append(el)
        else:
            i = bisect_left(cache, el)
            cache[i] = el

    print(cache, "\n" , len(cache))
    

if __name__ == "__main__":
    solution2()
