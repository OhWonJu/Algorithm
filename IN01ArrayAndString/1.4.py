## 회문 순열 ##

## 시간복잡도 O(N)
## case1: 문자열의 길이가 짝수인 경우-> 모든 문자가 짝수 개
## case2: 문자열의 길이가 홀수인 경우 -> 한 문자를 제외하고 나머지 문자는 짝수 개
## 단 공백은 예외
def Solution():
  testString = input("문자열을 입력하시오: ")
  result = isPalindromePermutation(testString)
  printResult(result)

def isPalindromePermutation(string):
  s = string.replace(" ", "")
  table = {}
  makeTable(table, s)
  table = isPair(table)
  if(len(s) % 2 == 0):
    if(len(table) != 0):
      return False
    else: return True
  else:
    if(len(table) != 1):
      return False
    else: return True

def makeTable(table, string):
  for key in string:
    if(not(key in table)):
      table[key] = 1
    else:
      table[key] += 1

def isPair(table):
  tempTable = {}
  for k, v in table.items():
    if(v % 2 != 0):
      tempTable[k] = v
  return tempTable

def printResult(result):
  if(result):
    print("회문 순열입니다.")
  else:
    print("회문 순열이 아닙니다.")

if __name__ == "__main__":
  Solution()

