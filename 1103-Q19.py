#연산자 끼워 넣기
#N 개의 수로 이루어진 수열이 주어짐
#수와 수사이에 넣을 N-1 개의 연산자가 주어짐
#연산자는 + - * // 4가지
#주어진 수의 순서는 변경 불가
#계산 시에 우선 순위 무시하고 무조건 순서대로 계산
#나눗셈은 나머지는 버리고 몫만 취함
#식의 결과가 최대인 것과 최소인 것을 구하는 프로그램 작성

#입력 조건
#1. 첫 줄에 수의 개수 N을 입력
#2. 다음 줄에 수열을 입력
#3. 그 다음 +개수 -개수 *개수 //개수를 차례로 입력(개수의 총합 N-1)

#출력 조건 : 첫 줄에 결과의 최대값/다음 줄에 결과의 최소값 출력

print('N 입력')
N = int(input())

print('N개의 수 입력')
number = list(map(int, input().split()))

print('연산자 정보 입력')
operation = list(map(int, input().split()))

#0 = +, 1 = -, 2 = *, 3 = //
from itertools import permutations
list0 = []
for i in range(len(operation)):
    for j in range(operation[i]):
        list0.append(i)

#연산 개수에 맞게 순열 계산
op_list = list(permutations(list0, len(list0)))

result_max = 0
result_min = int(1e9)

for i in op_list:
    a = number[0]
    #연산의 우선 순위 무시하고 차례대로 계산
    for j in range(len(list0)):
        if i[j] == 0:
            a += number[j+1]
        elif i[j] == 1:
            a -= number[j+1]
        elif i[j] == 2:
            a = a * number[j+1]
        elif i[j] == 3: #나눗셈 양수와 음수의 경우에 따라서 리턴값이 내 생각과 달랐음
            if a >= 0 and number[j+1] >= 0:
                a = a // number[j+1]
            elif a < 0 and number[j+1] < 0:
                a = a // number[j+1]
            else:
                a = -(abs(a) // abs(number[j+1]))
    print(i, a)
    result_max = max(a, result_max)
    result_min = min(a, result_min)

print(result_max)
print(result_min)

#자체 평가 : 생각보다 간단했음. // 연산의 리턴값이 생각과 달라서 조금 고민.