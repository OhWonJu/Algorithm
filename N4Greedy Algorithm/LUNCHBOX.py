# 도시락 데우기

# 스케쥴링 문제

# 개별 도시락을 데울 수 있음
# 데우는 시간, 먹는 시간
# 의 총합을 최소화 하는 방법을 찾고 싶다.

# 입력
# case(300)
## each case
## 데우는 시간(10,000)
## 먹는 시간(10,000)

# 출력
# 최소 시간 

# 먹는 시간이 가장 긴 순으로 하면?
# 선택한 옵션이 있는 최적해와
# 선택한 옵션이 배제된 최적해를 비교해보자..

# 매 부분 문제마다 먹는 시간이 가장 긴 옵션을 선택한다면..? 최적의 값을 구할 수 있을까?
# N번 부분문제의 이전 문제들의 순서 변경은 결국 N번에 영향을 미치지 않는다..?

def solution():
  case = 1
  foods = 3
  m = [2, 2, 2]
  e = [2, 2, 2]
  
  order = []
  for i in range(foods):
    order.append((m[i], e[i]))
    
  order.sort(key=lambda x: x[1], reverse=True)

  result = order[0][0] + order[0][1]
  for i in range(1, foods):
    result += (order[i][0] + order[i][1]) - order[i-1][1]
  
  print(result)
    

if __name__ == "__main__":
  solution()