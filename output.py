#출력은 print()를 이용
#print()는 출력 이후 기본적으로 줄바꿈 수행

a = 1
b = 2
print(a)
print(b)

answer = 10
#원래 문자열은 문자열끼리만 연산이 가능한데 str()로 answer를 문자열화 하면 연산이 가능
print('Answer is '+str(answer))
#연산이 아닌 , 로 표현할 경우 의도치 않은 공백이 삽입
print('Answer is ', str(answer))