# 곱하기 혹은 더하기

# 각 자리가 숫자로만 이루어진 문자열 S에 대해
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인..
# 숫자 사이를 + or x 했을 때 가장 큰 수
# 단 모든 연산은 왼쪽->오른쪽 순으로 이루어진다고 생각


def solution():
    case = input()

    result = int(case[0])

    for i in range(1, len(case)):
        num = int(case[i])
        if num <= 1 or result <= 1:
            result += num
        else:
            result *= num

    print(result)


if __name__ == "__main__":
    solution()
