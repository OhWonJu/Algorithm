# 모험가 길드

# 입력
# N(100,000)
# 공포도(N이하)

# 출력 최대 그룹 수

# 모험가가 모두 여행을 떠날 필요는 없다.

def solution():
    n = int(input())
    fear = list(map(int, input().split()))
    fear = fear[:n]
    fear.sort()

    groups = 0
    count = 0 
    for f in fear:
      count += 1
      if count >= f:
        groups += 1
        count = 0
      
    print(groups)




if __name__ == "__main__":
    solution()
