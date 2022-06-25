# 두 배열의 원소 교체

def solution():
    n, k = map(int, input().split())
    temp = list(map(int, input().split()))
    arrayA = temp[0:n]
    temp = list(map(int, input().split()))
    arrayB = temp[0:n]

    arrayA.sort()
    arrayB.sort(reverse=True)

    for i in range(n):
        if arrayA[i] < arrayB[i]:
            arrayA[i], arrayB[i] = arrayB[i], arrayA[i]
        else:
            break

    print(sum(arrayA))


if __name__ == "__main__":
    solution()
