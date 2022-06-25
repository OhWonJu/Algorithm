## 0 행렬 ##

# 시간복잡도 O(N + M)
# 해시테이블 사용
# 탐색 0인 행, 열을 저장
# 해당 행, 열을 0으로 치환
def Solution():
    # N x M
    matrix = [
        [1, 1, 1, 0],  # 0 0 0 0
        [0, 1, 0, 1],  # 0 0 0 0
        [1, 1, 1, 1],  # 0 1 0 0
    ]

    table = {}

    print(matrix)

    detectZero(matrix, table)
    setZeros(matrix, table)

    print(matrix)


def detectZero(matrix, table):
    row = len(matrix)
    col = len(matrix[0])
    for n in range(row):
        for m in range(col):
            if(matrix[n][m] == 0):
                if(n in table):
                    temp = []
                    temp.append(table[n])
                    temp.append(m)
                    table[n] = temp
                else:
                    table[n] = m


def setZeros(matrix, table):
    rowLen = len(matrix)
    colLen = len(matrix[0])

    for i in table.keys():
        for j in range(colLen):
            matrix[i][j] = 0

    # 너무 비효율적임! 행렬 정보를 저장할 수 있는 다른 자료구조를 생각해보자~ 병신아!
    row = []
    for inner_list in list(table.values()):
        if(type(inner_list) == int):
            row.append(inner_list)
        if(type(inner_list) == list):
            for data in inner_list:
                row.append(data)

    for i in row:
        for j in range(rowLen):
            matrix[j][i] = 0


# 공간 효율을 좀 더 높히는 방법 .
# 첫 행, 첫 열에 0정보를 저장 -> 공간복잡도를 O(1)로 낮춤
def Solution2():
    # N x M
    matrix = [
        [1, 1, 1, 0],  # 0 0 0 0
        [0, 1, 0, 1],  # 0 0 0 0
        [1, 1, 1, 1],  # 0 1 0 0
    ]

    print(matrix)
    setZeros(matrix)
    print(matrix)


def setZeros(matrix):
    # 첫 행, 열을 정보 저장용으로 사용할 것이기 때문에 첫 행, 열에 0이 있는지에 대한
    # 여부를 잃게 됨.. 그래서 요렇게 사용
    rowHasZero: bool = False
    colHasZero: bool = False

    # 첫 행에 0이 있는지 확인
    for j in range(len(matrix[0])):
        if(matrix[0][j] == 0):
            rowHasZero = True
            break
    # 첫 열에 0이 있는지 확인
    for i in range(len(matrix)):
        if(matrix[i][0] == 0):
            colHasZero = True
            break

    # 나머지 배열에 0이 있는지 확인
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j] == 0):
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(len(matrix)):
        if(matrix[i][0] == 0):
            nullifyRow(matrix, i)
    for j in range(len(matrix[0])):
        if(matrix[0][j] == 0):
            nullifyCol(matrix, i)

    if(rowHasZero):
        nullifyRow(matrix, 0)
    if(colHasZero):
        nullifyCol(matrix, 0)


def nullifyRow(matrix, row):
    for j in range(len(matrix[0])):
        matrix[row][j] == 0


def nullifyCol(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0


if __name__ == "__main__":
    # Solution()
    Solution2()
