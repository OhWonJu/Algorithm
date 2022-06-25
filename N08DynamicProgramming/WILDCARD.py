# 와일드 카드

# 종료 조건, 순차적으로 검증
# 와일드패턴의 끝에 도달 => 패턴에 *가 하나도 없는 경우. 패턴과 문자열의 길이가 같아야만 대응이라 판단
# 문자열의 끝에 도달 => 패턴이 남아있는 경우. 남은 패턴이 *로만 이루어져있어야만 대응
# 문자열과 와일드패턴의 문자가 일치하지 않음 => 대응 실패
# 패턴의 *를 만난 경우 => 대응 글자수를 모르기 때문에 순회하며 모든 가능성을 검사


import re


def solution(wild, case):
    cache = [[-1 for _ in range(len(case)+1)] for _ in range(len(wild)+1)]

    def pattern_matching(w, s):
        # 메모이제이션
        if cache[w][s] != -1:
            return cache[w][s]
        if w < len(wild) and s < len(case) and (wild[w] == '?' or wild[w] == case[s]):
            cache[w][s] = pattern_matching(w+1, s+1)
            return cache[w][s]
        # 패턴의 끝에 도달한 경우 - case도 끝이면 true
        if w == len(wild):
            cache[w][s] = 1 if s == len(case) else 0
            return cache[w][s]
        # 패턴이 *를 만난 경우
        if wild[w] == '*':
            # *에 몇글자를 대응할지를 재귀로 확인
            if pattern_matching(w+1, s) == 1 or (s < len(case) and pattern_matching(w, s+1) == 1):
                cache[w][s] = 1
                return cache[w][s]
        cache[w][s] = 0
        return cache[w][s]

    pattern_matching(0, 0)
    return cache[len(wild)][len(case)] == 1


def solution1(wild, case):
    pyWild = wild.replace("*", ".*").replace("?", ".")
    p = re.compile(pyWild)
    m = p.match(case)
    if m == None:
        return False
    else:
        return True


if __name__ == "__main__":
    wild = "*bb*"
    cases = ["help", "papa", "babbac"]
    result = []
    for case in cases:
        # if (solution1(wild, case) == 1):
        #    result.append(case)
        if solution1(wild, case):
            result.append(case)
    print(result)
