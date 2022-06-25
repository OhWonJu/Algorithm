# 문자열 뒤집기

# 0과 1로만 이루어진 문자열 S
# 0을 1로 1을 0으로 뒤집을 수 있음
# 최소한의 뒤집기로
# 문자열이 같은 문자로만 이루어지게 하기.
# 연속된 경우만 같이 뒤집기 가능.

# 어차피 all 0 아니면 1
def solution():
    case = input()
    changeTo0 = 0
    changeTo1 = 0

    if case[0] == "1":
        changeTo0 += 1
    else:
        changeTo1 += 1

    for i in range(1, len(case)):
        if case[i] != case[i-1]:
            if case[i] == "1":
                changeTo0 += 1
            else:
                changeTo1 += 1

    print(min(changeTo0, changeTo1))


if __name__ == "__main__":
    solution()
