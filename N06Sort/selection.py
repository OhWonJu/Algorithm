# 선택 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    minIndex = i
    for j in range(i+1, len(array)):
        if array[j] < array[minIndex]:
            minIndex = j
        # 파이썬에서 가능한 swap 문장... 다른 언어면 temp를 둬야겠지..
        array[i], array[minIndex] = array[minIndex], array[i]

print(array)

# 시간복잡도 O(N^2)
# 정렬해야할 원소가 100단위 이하이면 나쁘지 않은 선택지..
# 그래도 파이썬 내장 sort가 훨 빠름