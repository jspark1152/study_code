#함수를 사용하지 않으면 소스코드를 매번 작성해야하고 코드가 길어짐

def add(a,b):
    return(a+b)

print(add(1,2))

#return문 없이도 작성
def add(a,b):
    print('Result = ', a+b)

add(1,2)
add(b=3, a=2)

#함수 안에서 함수 밖의 변수(글로벌 변수) 데이터를 변경해야 하는 경우 global 키워드 이용
a=0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)

#파이썬에서 람다 표현식을 통해 함수를 간단하게 작성 가능
print((lambda a, b:a+b)(3,7))