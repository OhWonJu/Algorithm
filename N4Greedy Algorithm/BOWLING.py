# 볼링공 고르기

# 두 플레이어가 볼링공을 고르는 경우의 수를 구하기(단, 서로 다른 무게)
# 조합 문제?

# 입력
# 공의 갯수 N(1,000)
# 무게 종류 수 M(10)

def solution():
    #N, M = map(int, input().split())
    #
    #boll_list = list(map(int, input().split()))
    #boll_list = boll_list[0:N]
    
    N = 8
    M = 5
    boll_list = [1, 5, 4, 3, 2, 4, 5, 2]
    
    # 최적 선택이 뭘까.
    # 무게 1과 관련된 조합
    # 무게 2와 관련된 조합
    # 무게 3고 관련된 조합...
    # 각 무게별 갯수를 알아야한다?
    boll_weight = [0 for _ in range(M+1)]
    for boll in boll_list:
        boll_weight[boll] += 1  
    
    # 각 무게 이후와 계산하면 된다?
    # 이전은 이미 조합이 나왔기 때문에?
    result = 0
    for i in range(1, len(boll_weight)):
      N -= boll_weight[i] # 현 단계의 무게를 제외
      result += boll_weight[i] * N # 현 무게 * 다음 무게들

    print(result)        
  

if __name__ == "__main__":
  solution()