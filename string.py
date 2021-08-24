#문자열 변수를 초기화할 때는 큰따옴표나 작은따옴표를 이용
#다만 작성 중 문자열 안에 따옴표가 포함되어야 하는 경우가 있음
#기본적으로 큰따옴표로 구성된 문자열에는 내부적으로 작은 따옴표를 포함할 수 있음
#반대로 작은 따옴표로 구성했을 경우 큰 따옴표를 내부적으로 포함할 수 있음
#\ 를 이용하면 어느 상황에서건 원하는 만큼 포함시킬 수 있음

data = 'Hello World'
print(data)

data = 'Don\'t you know Python?'
print(data)
data = "Don't you know 'Python'?"
print(data)
data = "Don't you know \"Python\"?"
print(data)

#문자열 연산
a = "Hello"
b = "World"

print(a+' '+b)

a = 'String'
print(a*3)

#파이썬의 문자열은 내부적으로 리스트와 같이 처리
a = 'ABCDEF'
print(a[-1])
print(a[-4])
print(a[2])
print(a[2:-1])
print(a[2:])