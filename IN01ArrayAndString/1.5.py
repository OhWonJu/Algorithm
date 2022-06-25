## 하나 빼기 ##

## 시간복잡도 O(N + M)
##  
##
def Solution():
  string1, string2 = input().split(", ")
  if(abs(len(string1) - len(string2)) > 1):
    printResult(False)
    return 

  if(len(string1) <= len(string2)):
    printResult(compare(string1, string2))
  else:
    printResult(compare(string2, string1))


## 삽입 - 삭제
## 교체
def compare(string1, string2):
  string1Len = len(string1)
  string2Len = len(string2)
  
  editCount = 0
  str1 = 0
  str2 = 0
  while(str1 < string1Len and str2 < string2Len):
    if(editCount > 1):
      return False
    
    if(string1[str1] != string2[str2]):
      editCount += 1
      if(string1Len == string2Len): # 교체
        str1 += 1
    else: # 두 문자가 동일한 경우
      str1 +=1     
    str2 +=1 # 그 어떤 경우에도 길이가 긴 문자의 인덱스는 증가
  return True


def printResult(result):
  if(result):
    print("True")
  else:
    print("False")

if __name__ == "__main__":
  Solution()

