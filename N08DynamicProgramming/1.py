
array = [[-1] * 3] * 3
#print(array)
# [[-1] * 3  요 부분은 -1이라는 원시 객체를 3번 반복해서 넣아주는거고]
print(id(array[0][0]))
print(id(array[0][1])) # 원시 객체의 주소..
array[0][1] = 2
print(id(array[0][0]))
print(id(array[0][1])) # 다른 원시 객체를 참조하게 되니까 주소 바뀜

# [[-1] * 3] * 3 요 부분은 [-1, -1, -1] 이라는 리스트 객체를 3번 복사해서 넣는것
# 그렇기 때문에 1차원의 값들은 결국 같은 리스트 객체를 가리키는 메모리 값이겠지.. 
print(id(array[0]))
print(id(array[1])) # 같은 객체를 가리킴...

array[1][1] = 0
print(array)

print(id(array[0]))
print(id(array[1])) # 같은 객체를 가리킴...

# 모든 행의 1번 컬럼이 변경됨을 확인할 수 있다...
# 다 같은걸 참조하고 있는 셈...

print("________________________")

# 그냥 다차원 초기화를 하고 싶으면...리스트 컴프리어쩌고...
array = [[-1 for _ in range(3)] for _ in range(3)]
print(array)

array[0][1] = 0
print(array)