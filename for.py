#반복문은 특정 소스코드를 반복적으로 실행하고자 할 때 사용
#while문과 for문이 있는데 대부분 for문이 짧고 간결함

#while문
i = 1
result = 0

while i<=9:
    result += i
    i += 1

print(result)

i = 1
result = 0

while i<=9:
    if i%2==1:
        result += i
    i += 1

print(result)

#for문
result = 0

for i in range(10):
    result += i

print(result)

result = 0
for i in range(10):
    if i%2==1:
        result += i

print(result)

scores=[90, 85, 77, 65, 97]

for i in range(5):
    if scores[i]>=80:
        print(i+1, '번 학생은 합격입니다.')

cheating_list={2, 4}

for i in range(5):
    if i+1 in cheating_list:
        continue #반복문 작동 중 continue를 만나면 다음 루프로 진입
    if scores[i]>=80:
        print(i+1, '번째 학생은 합격입니다.')

#반복문은 얼마든지 중첩 가능
for m in range(2,10):
    for n in range(1,10):
        print(m, 'X', n, '=', m*n)
