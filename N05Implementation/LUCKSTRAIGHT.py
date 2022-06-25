# 숫자를 문자열로 파싱
# 다시 숫자로 파싱

# 입력 정수 N(10 ~ 99,999,999)

def solution():
    # N = int(input()) 
    #N = 7755
    #N = list(map(int, str(N)))
    # 애초에 문자열로 입력 받으면 된다.
    # N = input()
    N = "7755"
    N = list(map(int, N))
    harf_point = round(len(N) / 2)
    # print(harf_point)
    summery = 0
    summery += sum(N[:harf_point])
    summery -= sum(N[harf_point:])
    
    if summery == 0:
      print("LUCKY")
    else:
      print("READY")



if __name__ == "__main__":
  solution()