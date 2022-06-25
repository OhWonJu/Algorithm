# 문자열 재정렬

# 알파벳 대문자와 숫자
# 대문자는 오름차순, 숫자는 더해서 마지막에 배치

# 계수 정렬을 응용하면 되지 않을까?
import re
from unittest import result


def solution():
    # string = input()
    string = "AJKDLSI412K4JSJ9D"
    count = [0 for _ in range(26)]
    number_summery = 0
    
    for s in string:
      if ord(s) >= 65:
          count[ord(s) - 65] += 1
      else:
        number_summery += int(s)
    
    result = ""
    for i in range(len(count)):
      result += chr(i + 65) * count[i]
    if number_summery > 0:
      result += str(number_summery)
  
    print(result)


def solution2():
    # string = input()
    string = "AJKDLSI412K4JSJ9D"
    count = [0 for _ in range(26)]
    number_summery = 0
    
    result = []
    value = 0
    for c in string:
      if c.isalpha():
        result.append(c)
      else: value += int(c)
      
    result.sort()
    
    if value > 0:
      result.append(str(value))
      
    # 리스트를 문자열로 변환  
    print("".join(result))

if __name__ == "__main__":
    solution2()