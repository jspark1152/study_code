#파이썬에서는 집합을 처리하기 위한 집합 자료형을 제공
#기본적으로 리스트 혹은 문자열을 이용
#단, 중복을 허용하지 않으며 순서가 없음

#집합 자료형 촉화 방법
data = set([1, 1, 1, 2, 2, 3, 4, 4, 5])
print(data)

data = {1, 1, 1, 2, 2, 3, 4, 4, 5}
print(data)
#print(data[0]) Set에는 순서가 없기에 인덱싱이 불가

#집합 자료형의 연산
# | : 합집합
# & : 교집합
# - : 차집합

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

print(a|b)
print(a&b)
print(a-b)

#add() : 데이터 값 추가
#update() : 여러 데이터 값을 추가
#remove() : 특정 데이터 값을 제거

data = {1, 2, 3}
print(data)

data.add(4)
print(data)

data.update([5, 6])
print(data)

data.remove(3)
print(data)