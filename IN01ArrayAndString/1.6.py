## 문자열 압축 ##

## 시간복잡도 O(N)
## 해시테이블을 사용
def Solution():
  originStr: str = input("문자열을 입력: ")
  result = zipString(originStr)
  printResult(result)

def zipString(originStr):
  originLen = len(originStr)
  table = {}

  for key in originStr:
    if(key in table):
      table[key] += 1
    else:
      table[key] = 1
  
  zipedStr: str = ""
  for k, i in table.items():
    zipedStr += k
    zipedStr += str(i)
  
  return(zipedStr if len(zipedStr) <= originLen else originStr)

def printResult(result):
  print(result)

if __name__ == "__main__":
  Solution()


