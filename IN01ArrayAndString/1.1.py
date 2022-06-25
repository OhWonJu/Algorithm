## 문자열 중복 확인 ##

## 추가 자료구조를 사용한 알고리즘
## 시간복잡도 O(N), 공간복잡도 O(C) 단 ASCII기반이라면 O(1)이라 볼 수 있다.
## 해시테이블을 사용
## ASCII 기반 -> 전체 문자열이 128을 넘으면 필연적으로 중복
def SolutionWithExtraDataStructure():
  testString: str = input("문자열 입력: ")
  result: bool = checkDuplication(testString)
  printResult(result)

def checkDuplication(testString):
  # 기저 조건
  if(len(testString) > 128):
    return False
  table: dict = {}
  for key in testString:
    print(key)
    if(key in table): 
      return False
    else:
      table[key] = ord(key)
  return True
##

## 공간복잡도를 줄이는 방법
## 시간복잡도 O(N), 공간복잡도를 1/8로 줄일 수 있다.
## 비트 벡터를 사용
## 문자열이 a ~ z으로만 구성되어 있다고 가정.
def SolutionWithExtraDataStructure2():
  testString: str = input("문자열 입력:")
  result: bool = checkDuplication2(testString)
  printResult(result)

def checkDuplication2(testString):
  # 기저 조건
  if(len(testString) > 26):
    return False
  checker: int = 0; # 하나의 Intger 변수의 비트 벡터를 통해 중복 결과를 저장
  for c in testString:
    val: int = ord(c) - ord('a')
    if((checker & (1 << val)) > 0): # 본래 비트 벡터와 해당 숫자가 위치하는 비트 벡터를 비교
      return False
    checker  |= (1 << val)
  return True
##

## 추가 자료 구조를 사용하지 않는 방법
## 입력받은 문자열을 조작 가능한 경우
## 정렬 -> 이전 문자열과 비교
## 시간복잡도 O(NlongN), 추가 공간복잡도 발생
def SolutionWithOutExtraDataStructure():
  testString: str = input("문자열 입력:")
  result: bool = checkDuplication3(testString)
  printResult(result)

def checkDuplication3(testString):
  if(len(testString) > 128):
    return False
  sortedStr = sorted(testString);
  for i in range(len(sortedStr)):
    if(i+1 == len(sortedStr)):
      return True
    if(sortedStr[i] == sortedStr[i+1]):
      return False
  return True

def printResult(result):
  if(result == True):
    print("중복된 문자열이 없습니다.")
  else:
    print("중복된 문자열이 있습니다.")

if __name__ == "__main__":
  #SolutionWithExtraDataStructure()
  #SolutionWithExtraDataStructure2()
  SolutionWithOutExtraDataStructure()


