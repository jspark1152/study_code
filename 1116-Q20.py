#감시 피하기
#N X N 크기의 복도의 특정 위치에 선생님, 학생, 장애물이 있음
#학생 몇 명이 수업 시간에 몰래 복도에 나왔는데 선생님의 감시에 들키지 않는 것이 목표
#선생님은 상하좌우 4방향으로 감시를 진행
#단, 장애물에 가려진 학생은 볼 수 없음
#학생들은 복도의 빈칸 중에서 장애물 설치할 위치를 골라 3개의 장애물을 설치
#선생님의 감시로부터 모든 학생이 피할 수 있는지 확인

#입력 조건
#1. 첫 줄에 자연수 N이 주어짐(3이상 6이하)
#2. 다음줄부터 N개의 줄에 복도의 정보가 주어짐
#각 행은 N개의 원소가 주어지며 S(학생) / T(선생님) / X(빈공간) 으로 입력

#출력 조건 : 정확히 3개의 장애물을 설치하여 모든 학생들이 감시로부터 피할 수 있는지 여부를 출력

print('자연수 N 입력')
N = int(input())

print('복도 정보 입력')
corridor = []
for i in range(N):
    corridor.append(list(map(str, input().split())))

print(corridor)

#장애물 3개를 설치.. 모든 경우의 수를 따져야 하나?

#빈 공간 파악
empty = []
for i in range(N):
    for j in range(N):
        if corridor[i][j] == 'x':
            empty.append((i, j))

#교사 위치 파악
teacher = []
for i in range(N):
    for j in range(N):
        if corridor[i][j] == 't':
            teacher.append((i, j))

print(teacher)

from itertools import combinations

block = list(combinations(empty, 3))

import copy

#장애물 설치 함수, 변수 복제 필요
def setup_block(i):
    corr0 = copy.deepcopy(corridor)
    for a in i:
        corr0[a[0]][a[1]] = 'o'
    return corr0

#교사 감시 함수
def observe(corr0):
    result = 'YES'
    for i in teacher:
        #up
        a = 0
        while i[0]-a != 0:
            a += 1
            if corr0[i[0]-a][i[1]] == 'x':
                pass
            elif corr0[i[0]-a][i[1]] == 'o':
                break
            elif corr0[i[0]-a][i[1]] == 's':
                result = 'NO'
                break
        
        #down
        b = 0
        while i[0]+b != N-1:
            b += 1
            if corr0[i[0]+b][i[1]] == 'x':
                pass
            elif corr0[i[0]+b][i[1]] == 'o':
                break
            elif corr0[i[0]+b][i[1]] == 's':
                result = 'NO'
                break
        
        #left
        c = 0
        while i[1]-c != 0:
            c += 1
            if corr0[i[0]][i[1]-c] == 'x':
                pass
            elif corr0[i[0]][i[1]-c] == 'o':
                break
            elif corr0[i[0]][i[1]-c] == 's':
                result = 'NO'
                break
                
        #right
        d = 0
        while i[1]+d != N-1:
            d += 1
            if corr0[i[0]][i[1]+d] == 'x':
                pass
            elif corr0[i[0]][i[1]+d] == 'o':
                break
            elif corr0[i[0]][i[1]+d] == 's':
                result = 'NO'
                break
    return result


for i in block:
    #장애물 설치
    corr0 = setup_block(i)

    #감시 Check
    result = observe(corr0)
    if result == 'YES':
        break

print(result)

#자체 평가 : 꽤 복잡했으나 엄청 어렵진 않았음. Step 별로 작성하니 수월.
#observe 함수 작성할 때 조건문 실수로 == 이라고 하는 바람에 살짝 헤맴;;