# 외발 뛰기

# 아래 혹은 오른쪽으로만 이동 가능하다.
# 끝점에 도달하는 방법이 존재하는지를 반환하라.

# 사실 BFS의 양방향 탐색이 더 낫겠지


map_size = 5
# 아무리 가도 도달할 수 없다...
maps = [[1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 2, 0]]


def solution():
    # 완전탐색 재귀로 시작하라.
    def jump(y, x):
        # 기저 조건을 먼저 설정하라
        # 기저 조건 - 맵을 넘어서면...
        if y >= map_size or x >= map_size:
            return False
        # 기저 조건 - 도착 지점에 도달한다.
        if maps[y][x] == 0:
            return True
        step = maps[y][x]
        # 아래 혹은 오른쪽으로 진행한다.
        # 두 경우 중 목표지점에 도달하면 된다.
        return jump(y+step, x) or jump(y, x+step)

    if jump(0, 0):
        print("도착할 수 있음")
    else:
        print('도착할 수 없음')
    # 엄청난 연산 시간이 필요함..
    # n^2의 연산시간..
    # 도착할 수 없음을 알게 됬지만 계속 연산하겠지..


def solution1():
    # 동적 계획법 적용
    # 메모이제이션 캐시 생성
    cache = [[-1] * map_size] * map_size

    def jump(y, x):
        # 기저 조건 - over range
        if y >= map_size or x >= map_size:
            return False
        # 기저 조건 - 도착 지점에 도달한다.
        if maps[y][x] == 0:
            return True
        ret = cache[y][x]
        # 캐시에 값이 존재한다면 즉시 반환
        if cache[y][x] != -1:
            return ret
        # 캐시에 값이 존재하지 않는다면 기존 완전탐색처럼..
        step = maps[y][x]
        # 해당 경로를 통해서 목표지점에 갈 수 있는지 없는지를 저장...
        # 재귀의 경우 목표지점 근처에서부터 메모이제이션을 하겠지.
        ret = jump(y+step, x) or jump(y, x+step)
        return ret

    if jump(0, 0):
        print("도달 할 수 있음")
    else:
        print("도달 할 수 없음")


if __name__ == "__main__":
    solution1()
