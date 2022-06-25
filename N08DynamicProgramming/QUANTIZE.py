# 양자화

# 양자화 과정은, 더 넓은 범위를 갖는 값들을 작은 범위를 갖는 값들로 근사해 표현함.
# == 자료를 손실 압축하는 과정

# 1000이하의 자연수로 구현된 수열을 S가지의 자연수만을 사용하여 양자화 하여라.
# 단 숫자별 오차 제곱의 합을 최소화하라.
# 결과값을 출력하라.


# 최소 시작 단위는... S?
# 매반 단계를 거칠 때마다 양자값을 구할 수 없다...메모이제이션을 해도 시간이 오래걸린데
# 부분 문제가 너무 많은 경우!!

# 부분문제가 많은 경우,,, 답이 항상 어떤 구조를 가질 것이라고 예측하고 그것을 강제하는 방법이 있다.

# 양자화 결과는 원소의 순서와 상관없다..
# 정렬을 하면 유사한 값들이 가까이 위치하게 된다?
# 이들을 적절히 분할해서 양자화하면....!
# 문제의 구조를 강제 -> 수열을 S개의 묶음으로 나누는 문제가 된다잉

INF = int(1e9)

# 이중 for문을 돌면서 form - to 간의 편차값을 구함
# 이전 단계까지 몇개의 s를 썻는지 기억해야겠지?
# 그거에서 남은거 만큼 할끄야
# 그래가꼬 결과를 계산할끄야 1개쓴거랑 2개쓴거랑 ..n개 쓴거랑 비교해서 그중 가장 작은걸 저장하면 된다 아녀?
#


def solution():
    # frm -> to의 최소 오차합
    def min_error(frm, to):
        if frm >= to:
            return 0
        # frm - to 간의 합을 구한다
        s = pSum[to] - (0 if frm == 0 else pSum[frm-1])
        # 구간의 제곱합
        sqS = pSqSum[to] - (0 if frm == 0 else pSqSum[frm-1])
        # 평균 반올림
        mean = round(s / (to - frm + 1))
        # 구간 제곱 오차는 ... 구간 제곱 합 - 2*구간평균오차*구간합 + 구간평균오차제곱 ?
        result = sqS - 2 * mean * s + mean * mean * (to-frm+1)
        return result

    #array = [1, 2, 3, 4, 5]
    array = [1, 744, 755, 4, 897, 902, 890, 6, 777]
    #array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #array = [161, 164, 178, 184]
    s = 3
    pSum = [array[0]]  # 0~ i 까지의 부분합 저장
    pSqSum = [pow(array[0], 2)]  # 0~ i 까지의 제곱 부분합 저장

    array.sort()
    for i in range(1, len(array)):
        pSum.append(pSum[i-1] + array[i])
        pSqSum.append(pSqSum[i-1] + pow(array[i], 2))

    MSE = 0
    particleMSE = []
    frm = 0
    for to in range(2, len(array)):
        ops1 = min_error(frm, to-1)
        ops2 = min_error(frm, to)
        if ops1 + min_error(to, len(array)-1) < ops2 + min_error(to+1, len(array)-1) and s > 1:
            print("SEPER: ", ops1, to)
            s -= 1
            frm = to
            particleMSE.append(ops1 if to == 2 else MSE)
            MSE = 0
        else:
            print("INCLUD: ", ops2)
            MSE = ops2
    particleMSE.append(MSE)
    print(sum(particleMSE))


if __name__ == "__main__":
    solution()
