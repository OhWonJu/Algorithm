# 퀵 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:
        return
    # Hoare Partition
    pivot = start
    left = start+1
    right = end
    while left <= right:
        # pivot보다 큰 값을 찾는다.
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # pivot 보다 작은 값을 찾는다
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 두 iter가 엇갈린 경우
        if left > right:
            # 작은 값과 pivot을 교체
            array[right], array[pivot] = array[pivot], array[right]
            pivot = right
        else:
            array[left], array[right] = array[right], array[left]
        #print(left, right)
    # 분할 이후 재귀
    quick_sort(array, start, pivot-1)
    quick_sort(array, pivot+1, end)


quick_sort(array, 0, len(array)-1)
print(array)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 파이썬 구문 사용


def quick_sort_py(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]  # pivot을 제외한 list
    # 리스트 컴프리헨션, 직관적이지만 pivot과의 비교횟수 증가.
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort_py(left_side) + [pivot] + quick_sort_py(right_side)


print(quick_sort_py(array))
