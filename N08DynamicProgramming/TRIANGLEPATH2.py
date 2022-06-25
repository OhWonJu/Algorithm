# 삼각 최대 경로 수 세기

# TRIANGELPATH 문제에서 최대 경로의 수를 구하라

# 경로 부분 구간 간의 최대합을 구한다.
from copy import copy


def solution(n, triangle):
    cache = [[-1 for _ in range(y+1)] for y in range(n)]

    def get_largest_path():
        cache[-1] = copy(triangle[-1])
        for row in range(n-2, -1, -1):
            for col in range(len(triangle[row])):
                cache[row][col] = max(
                    cache[row+1][col], cache[row+1][col+1]) + triangle[row][col]

    get_largest_path()
    print(cache)

    # 각 단계에서 분기할 수 있는 수를 구한다면...?
    pathCache = [[1 for _ in range(y+1)] for y in range(n)]

    # 각 부분 경로에서의 최대합 경로 수를 구한다.
    #                     pathCahce(y+1, x)
    #  pathCahce(y, x) =  pathCahce(y+1, x+1)
    #                     pathCahce(y+1, x) + pathCahce(y+1, x+1)
    def get_number_of_paths():
        for row in range(n-2, -1, -1):
            for col in range(len(cache[row])):
                if cache[row+1][col] > cache[row+1][col+1]:
                    pathCache[row][col] = pathCache[row+1][col]
                elif cache[row+1][col] < cache[row+1][col+1]:
                    pathCache[row][col] = pathCache[row+1][col+1]
                else:
                    pathCache[row][col] = pathCache[row+1][col] + pathCache[row+1][col+1]

    get_number_of_paths()
    print(pathCache[0])


if __name__ == "__main__":
    triangle = [[9],
                [5, 7],
                [1, 3, 2],
                [3, 5, 5, 6]]
    n = len(triangle)
    solution(n, triangle)
