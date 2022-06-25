## 문자열 회전 ##

# 시간복잡도 O(N)
# 회전 분기가 되는 문자열을 찾으면 됨.
# 회전 분기가 되는 문자열을 기준으로 x, y로 분리되고 x, y의 연속인 셈
# xyxy와의 문자 비교를 수행하면 문자열 회전을 만족하는지 확인할 수 있음
def Solution():
    str1, str2 = input("문자열을 입력하시오: ").split(", ")
    result = isRotated(str1, str2)
    print(result)


def isRotated(str1, str2):
    # 기저 조간
    # 1. 길이가 같아야 함. 빈문자열이 아니어야함
    if((len(str1) > 0 and len(str2) > 0) and (len(str1) == len(str2))):
        testStr = str1 + str1
        if str2 in testStr:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    Solution()
