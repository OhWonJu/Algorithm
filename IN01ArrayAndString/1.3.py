## 문자열 치환 ##

## 시간복잡도 O(N)
## replace 함수가 있지만..
## replace를 구현한다는 느낌으로 해결해봄 C++ 스타일
def Solution():
  inputString, inputLen = input("문자열을 입력하시오: ").split(", ")
  inputLen = int(inputLen)
  count: int = 0
  for c in inputString:
    if(c == " "):
      count += 1
  
  urlLen: int = inputLen + count 
  url: str = "" ## 정적 배열이라 생각 -> urlLen 길이 만큼
  for i in range(inputLen):
    if(inputString[i] == " "):
      url += '%'; url += '2'; url += '0'
      i += 3
    else:
      url += inputString[i]

  print("입력: {0} \n출력: {1}" .format(inputString, url))

if __name__ == "__main__":
  Solution()

