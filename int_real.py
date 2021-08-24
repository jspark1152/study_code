a = 1000 #positive int
print(a)

a = -7 #negative int
print(a)

a = 0 #zero
print(a)

a = 157.93 #positive real
print(a)

a = 1837.2 #negative real
print(a)

a = 5. #positive real - 소수부가 0일 때 0 생략
print(a)

a = -.7 #negative real - 정수부가 0일 때 0 생략
print(a)

a = 1e9 #1e는 10으로 뒤에 9는 10의 거듭제곱을 의미
print(a)

a = 75.25e1 #75.25 * 10^1
print(a)

a = 3954e-3 #3954 * 10^(-3)
print(a)

a = 0.3 + 0.6
print(a)

a = round(a, 4) #round( , n) : 소수 n+1 번째 자리에서 반올림
print(a)

if a==0.9:
    print(True)
else:
    print(False)