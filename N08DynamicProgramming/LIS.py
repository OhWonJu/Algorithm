# # 최대 증가 부분 수열
# # 증가 부분 수열 중 가장 긴 것을 찾아라
# # 동적 계획법 대표 연습 문제..

# from re import sub


# def solution():
#     array = [5, 6, 7, 1, 2, 7, 3, 4]

#     cache = [-1] * (len(array) + 1)

#     def lis(start):
#         # 현재 원소보다 큰 부분 수열을 구한다
#         if cache[start] != -1:
#             return cache[start]
#         cache[start] = 1
#         for n in range(start+1, len(array)):
#             # 0에서 시작하면 0번 기준 이후 부분 집합들만 하니까..
#             if start == -1 or array[start] < array[n]:
#                cache[start] = max(cache[start], 1+lis(n))
#         return cache[start]

#     print(lis(-1)-1)


# if __name__ == "__main__":
#     solution()
#
#

from bisect import bisect_left


def solution():
    # lis의 길이를 구하기. 이분 검색
    array = [5, 6, 1, 7, 2]
    cache = [array[0]]

    for i in range(1, len(array)):
        # 마지막 원소가 지금 원소보다 작을 경우
        if cache[-1] < array[i]:
            cache.append(array[i])
        # 지금 원소가 작은 경우
        else:
            idx = bisect_left(cache, array[i])
            cache[idx] = array[i]

    print("lenght: ", len(cache))


def solution1():
    # lis의 길이 뿐만이 아니라 원소까지 구해서 출력
    array = [5, 6, 1, 7, 2]
    cache = [1 for _ in range(len(array))]

    # O(N^2)
    for i in range(len(array)):
        for j in range(i, len(array)):
            # 마지막 원소로 했을 때의 최대 길이 구하기.
            if array[i] < array[j]:
                cache[j] = max(cache[i]+1, cache[j])
    longest_len = max(cache)
    print(array)
    print(cache)
    print("Length:", longest_len)

    lis = []
    longest_idx = cache.index(longest_len)
    while longest_idx >= 0:
        if cache[longest_idx] == longest_len:
            lis.append(array[longest_idx])
            longest_len -= 1
        longest_idx -= 1
    lis.reverse()
    print(lis)


def solution2():
    array = [5, 6, 7, 1, 2]
    cache = []

    def lis(start):
        if start >= len(array):
            return
        if len(cache) == 0 or cache[-1] < array[start]:
            cache.append(array[start])
        else:
            idx = bisect_left(cache, array[start])
            cache[idx] = array[start]
        lis(start+1)

    lis(0)
    print(len(cache))
    print(cache)


if __name__ == "__main__":
    solution1()
