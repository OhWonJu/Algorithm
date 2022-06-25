## 문자열 순열 확인 ##

## 해시테이블을 사용
## 문자 개수를 value로 저장
## 시간복잡도 O(N+M)
def Solution():
  testString1: str = input("문자열1 입력: ")
  testString2: str = input("문자열1 입력: ")
  # 기저 조건
  if(len(testString1) != len(testString2)):
    printResult(False)
    return
  table: dict = {}
  makeTable(table, testString1)
  result: bool = checkPermutation(table, testString2)
  printResult(result)

def makeTable(table, testString):
  for key in testString:
    if(not(key in table)):
      table[key] = 1
    else:
      table[key] += 1

def checkPermutation(table, testString):
  for key in testString:
    if(not(key in table)):
      return False
    else:
      table[key] -= 1
      if(table[key] <= 0):
        del(table[key])
  print(table)
  if(len(table) == 0):
    return True
  else:
    return False

def printResult(result):
  if(result == True):
    print("두 문자열은 순열 관계입니다.")
  else:
    print("두 문자열은 순열 관게가 아닙니다.")

if __name__ == "__main__":
  Solution()

