## 너드인가? 너드가 아닌가? 2 ##
from bisect import *


def Solution1():
    cases = [(72, 50), (57, 67), (74, 55), (64, 60)]
    coords = {}
    keys = []

    def isDominated(x, y):
        # 새 좌표가 지배되는지를 확인한다.
        # 지배 여부를 알 수 있는 방법은??
        # 새 좌표 왼쪽의 가장 오른쪽 x값에 대응되는 y 값이 새 좌표의 y 값보다 크면 새 좌표는 지배당한다.
        try:
            i = bisect(keys, x)
            # print(y < coords[keys[i]])
            return y < coords[keys[i]]
        except IndexError:
            # print("Err")
            return False

    def removeDominated(x, y):
        # 새 좌표가 지배하는 기존 좌표를 삭제해야 함.
        # isDominated에서 넘어왔다는건 새 좌표 오른쪽은 x가 크고 y가 작음!
        # 새 좌표 왼쪽의 y값이 작은 좌표를 찾아 지워야함.
        try:
            i = bisect(keys, x)
            if(i == 0):
                return
            i -= 1
            while(True):
                if(coords[keys[i]] > y):
                    break
                if(i == 0):
                    del(coords[keys[i]])
                    del(keys[i])
                    break
                else:
                    j = i - 1
                    del(coords[keys[i]])
                    del(keys[i])
                    i = j
        except IndexError:
            return

    def registered(x, y):
        if(isDominated(x, y)):
            return len(coords.keys())
        removeDominated(x, y)
        coords[x] = y
        insort(keys, x)
        print(coords)
        return len(coords.keys())

    totalCount = 0
    for x, y in cases:
        totalCount += registered(x, y)
        # print(totalCount)
    print(totalCount)


if __name__ == "__main__":
    Solution1()
