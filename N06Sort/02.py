# 성적이 낮은 순서로 학생 출력하기

# count 정렬...혹은 라이브러리..
# 데이터의 수가 많을 수록 count가 유리

def solution():
    n = int(input())
    array = []
    max_value = 0
    for _ in range(n):
        temp = input().split()
        try:
            temp[1] = int(temp[1])
        except:
            temp[1] = 0
        max_value = max(max_value, temp[1])
        array.append(temp)

    count = [[] for _ in range(max_value+1)]
    for i in range(len(array)):
        index = array[i][1]
        value = array[i][0]
        count[index].append(value)

    for array in count:
        if len(array) < 1:
            continue
        for data in array:
            print(data, end=" ")


if __name__ == "__main__":
    solution()
