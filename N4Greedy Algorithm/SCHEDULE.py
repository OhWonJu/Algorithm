# 회의실 예약

# 가장 빨리 끝나는 회의를 선택하고
# 이와 겹치는 회의는 지운다.

# 대부분의 그리디의 정당정 증명은 일정한 패턴을 가짐
# 1. 탐욕적 선택 속성 Greedy Choice Property
## 탐욕적 선택은 항상 최적해로 가는 길 중 하나임.
## "그리디 선택을 포함하는 최적해가 반드시 존재한다." 라는 속성
## - 최초 선택했던것에서.. 가장빨리 끝나는 선택이 아닌경우..
## - 최초 선택을 가장 빨리 끝나는 선택으로 바꿔도 최적해에 갈 수 있음!
# 2. 최적 부분 구조 Optimal Substructure
## 부분 문제의 최적해에서 전체 문제의 최적해를 만들 수 있음을 보여야함.
## 당연해서...따로 증명할 필요가 없는 경우가 대부분.
## - 첫 선택 이후 걸러내지고 남은 회의 중 최대한 많은 회의를 선택해야함..

# [begin - end)

def solution():
  #n = int(input())
  n = 11
  schedules = [(0, 7), (2, 4), (3, 5), (1, 4), (2, 7), (2, 4), (5, 9), (6, 9), (8, 9), (9, 10), (8, 10)]
  schedules.sort(key=lambda x: x[1])

  # 다음 회의가 가장 빨리 시작 할 수 있는 시간
  earliest = 0 
  # 결과s
  selected = 0
  confirmedSchedules = []
  for s in schedules:
    if earliest <= s[0]:
      earliest = s[1]
      selected += 1
      confirmedSchedules.append(s)

  print(selected, "\n", confirmedSchedules)
  


if __name__ == "__main__":
  solution()