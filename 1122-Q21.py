#인구 이동
#N X N 크기의 땅이 있음
#각 땅에는 나라가 하나씩 존재
#r행 c열의 나라에는 A[r][c]명이 살고 있음
#인접한 나라 사이에는 국경선이 존재
#인구이동은 다음과 같이 진행, 아래 방법에 의해 이동이 없을 때까지 지속
#1. 국경선을 공유하는 두 나라의 인구 차이가 L 이상 R 이하 라면, 두 나라가 공유하는 국경선을 하루 동안 open
#2. 1번 조건에 의해 열어야 하는 국경선이 모두 열렸다면, 인구 이동을 시작
#3. 국경선이 열려 있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 '연합'이라고 함
#4. 연합을 이루고 있는 각 칸의 인구수는 (연합 인구수)/(연합을 이루고 있는 칸의 개수)가 됨. 소수점은 버림
#5. 연합을 해체하고, 모든 국경선을 닫음
#각 나라의 인구수가 주어졌을 때, 인구 이동이 몇 번 발생하는지 구하는 프로그램을 작성

#입력조건
#1. 첫 줄에 N, L, R이 주어짐
#2. 다음 줄부터 N줄에 걸쳐 각 나라의 인구수가 주어짐
#3. 인구 이동이 발생하는 횟수가 2,000번보다 작거나 같은 입력만 주어짐

#출력 조건 : 인구 이동이 몇번 발생하는지 출력

#음.. 굉장히 복잡해보임
#일단 당장에 인구 이동 방법이 머리속에서 정리가 안됨

print('N, L, R 입력')
N, L, R = map(int, input().split())

print('인구수 정보 입력')
population = []
for i in range(N):
    population.append(list(map(int, input().split())))

print(population)

#연합을 mark로 넘버링하면 좋을듯
mark0 = []
for i in range(N):
    mark0.append([0] * N)

#연합 함수를 재귀 형태로 표현
def united(i, j, a):
    mark[i][j] = a
    #up
    if i-1 >= 0:
        if abs(population[i-1][j] - population[i][j]) >= L and abs(population[i-1][j] - population[i][j]) <= R:
            if mark[i-1][j] == 0:
                united(i-1, j, a)
            
    #down
    if i+1 < N:
        if abs(population[i+1][j] - population[i][j]) >= L and abs(population[i+1][j] - population[i][j]) <= R:
            if mark[i+1][j] == 0:
                united(i+1, j, a)
        
    #left
    if j-1 >= 0:
        if abs(population[i][j-1] - population[i][j]) >= L and abs(population[i][j-1] - population[i][j]) <= R:
            if mark[i][j-1] == 0:
                united(i, j-1, a)
       
    #right
    if j+1 < N:
        if abs(population[i][j+1] - population[i][j]) >= L and abs(population[i][j+1] - population[i][j]) <= R:
            if mark[i][j+1] == 0:
                united(i, j+1, a)

stop = 0
result = 0
a = 1

import copy

while a == 1:
    #연합 구성
    mark = copy.deepcopy(mark0)
    for i in range(N):
        for j in range(N):
            if mark[i][j] == 0:
                united(i, j, a)
                a += 1
    print(mark) #연합 map
    print(a) #연합의 수
    
    #인구 이동이 불가한 경우는 국가 수와 연합 수가 일치할 때 break
    if a == N*N + 1:
        break
    
    #인구 이동
    for i in range(1, a):
        count = 0
        sum = 0
        for m in range(N):
            for n in range(N):
                if mark[m][n] == i:
                    count += 1
                    sum += population[m][n]
        div = sum // count #인구 배분
        for m in range(N):
            for n in range(N):
                if mark[m][n] == i:
                    population[m][n] = div
    print(population)
    result += 1
    a = 1 #a 값 초기화   

print(result)


    

