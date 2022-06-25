# 계수 정렬

# 데이터가 특정 범위만 표현할 경우 (정수)
# 데이터의 중복이 많은 경우..

# 데이터의 수를 배열에 저장한다
# O(N + K)의 시간 복잡도. (K = 가장 많이 중복된 데이터의 수) 정렬결과를 출력한다는 조건하에서..
# 출력안하면/??? O(N)만 걸릴듯.

# 데이터의 토탈 수가 많아도 표현범위가 한정적이면 매우 빠르게 sorting 가능

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8, 0 ,5 ,2, 1, 8, 1, 2, 0]

count = [0] * (max(array)+1) # 0~가장 큰 값

for i in range(len(array)):
  count[array[i]] += 1

resultStr  = ""
for i in range(len(count)):
  # 이러면 K를 피할 수 있는 거 아님?
  # 문자열 출력에 한에서만 인가..
  # 
  temp = (str(i) + " ") * count[i]
  resultStr += temp

print(resultStr)
