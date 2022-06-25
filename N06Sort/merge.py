# 병합 정렬...

def mergeSort(arr):
    # 병합 + 정렬
    def sort(left, right):
        # 기저 조건 : 두 수 사이의 간격이 최소 2 mid를 구할 수 있는 최소 범위
        if right - left < 2:
            return
        mid = (left+right) // 2
        sort(left, mid)
        sort(mid, right)
        merge(left, mid, right)

    def merge(left, mid, right):
        temp = []
        pt1, pt2 = left, mid
        # merge과정은 insert와 유사?
        while pt1 < mid and pt2 < right:
            if arr[pt1] < arr[pt2]:
                temp.append(arr[pt1])
                pt1 += 1
            else:
                temp.append(arr[pt2])
                pt2 += 1
        while(pt1 < mid):
            temp.append(arr[pt1])
            pt1 += 1
        while(pt2 < right):
            temp.append(arr[pt2])
            pt2 += 1
        for i in range(left, right):
            arr[i] = temp[i - left]

    return sort(0, len(arr))


if __name__ == "__main__":
    ls = [2, 3, 1, 4]
    mergeSort(ls)
    print(ls)