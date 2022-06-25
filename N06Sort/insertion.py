# 삽입 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            # 원소 밀어내기..
            array[j], array[j-1] = array[j-1], array[j]
        else:
            # target 원소 이전의 원소들은 정렬되었다 가정하기 때문에 swap이 멈추는 지점은 정렬이 되어있는것..
            break

print(array)