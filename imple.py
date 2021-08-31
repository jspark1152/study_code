#구현(implementation)이란 머릿 속 알고리즘을 소스코드로 바꾸는 과정
#문제 -- 풀이법 고민 -- 해결책 떠오름 -- 구현
#완전 탐색 : 모든 경우의 수를 주저 없이 다 계산
#시뮬레이션 : 문제에서 제시한 알고리즘을 한 단계씩 차례대로 수행

#메모리 제약
#파이썬에서 정수 데이터의 메모리는 크게 신경 안써도 됨
#단, 리스트가 문제
#코딩 테스트에서 보통 128~512MB로 메모리를 제한함
#리스트 길이가 1,000 인 경우 4 KB 메모리 할당;; > 길어질수록 비례하여 커짐
#따라서 길이가 긴 리스트를 여러 개 선언할 경우 문제가 발생할 수 있음

#보통 구현 유형 문제는 사소한 입력 조건 등을 명시해주며 문제 길이가 꽤 긴 편임

#예제 1 : 상하좌우
#여행가 A는 N X N 공간 위에 서 있음
#좌상단 좌표 = (1, 1), 우하단 좌표 = (N, N)
#여행 계획서에는 띄어쓰기를 기준으로 L, R, U, D 중 하나의 문자가 반복적으로 적혀있음
#이동 중 공간 밖으로 나갈 경우는 무시(횟수는 차감)
#계획서가 주어졌을 때 최종 A의 위치를 출력

#첫째 줄에 공간의 크기를 나타내는 N(1이상 100이하)이 주어짐
#둘째 줄에 여행가 A가 이동할 계획서 내용이 주어짐(1회 이상 100회 이하)

#출력 조건 : A가 최종적으로 도착할 지점의 좌표 (X, Y)를 공백으로 구분하여 출력

print('공간 크기 N을 입력')
N = int(input())

print('이동 계획서 입력')
plan = list(map(str, input().split()))

A_loc = [1, 1]

for i in plan:
    if i == 'R':
        A_loc[1] += 1
        if A_loc[1] > N:
            A_loc[1] -= 1
    if i == 'L':
        A_loc[1] -= 1
        if A_loc[1] < 1:
            A_loc[1] += 1
    if i == 'U':
        A_loc[0] -= 1
        if A_loc[0] < 1:
            A_loc[0] += 1
    if i == 'D':
        A_loc[0] += 1
        if A_loc[0] > N:
            A_loc[0] -= 1

print(A_loc[0], A_loc[1])
#자체 평가 : 10분 걸린듯? 아무래도 조건식을 너무 많이 쓴듯한 느낌?
#좌표 표현할 때 튜플로 선언하는 실수를 범할지도 모를듯(튜플 값은 변경 불가능)
#모범 답안이랑 전체적 흐름 차이는 없어보임

#예제 2 : 시각
#정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수

#첫째 줄에 정수 N(0이상 23이하)이 입력

#출력 조건 : 00시 00분 00초부터 N시 59분 59초 까지의 모든 시각 중 3이 포함되는 모든 경우의 수를 출력

print('시각 N 을 입력')
N = int(input())

# 00분 00초 ~ 59분 59초 까지 경우의 수 10*6*10*6 = 3600

#반대로 3이 하나도 포함 안되는 경우를 구하고 전체에서 제외

# 00분 00초 ~ 59분 59초 까지 3이 하나도 없는 경우의 수 9*5*9*5 = 45^2

no_3 = 45*45

count = 3600 - no_3

result = 0
for i in range(N+1):
    if i != 3 and i != 13 and i != 23:
        result += count
    else:
        result += 3600

print(result)
#자체 평가 : 뭔가 수학 문제 풀이하는 느낌

print('시각 N 을 입력')
N = int(input())

count = 0
# t : m : s
for t in range(N+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(s):
                count += 1
            elif '3' in str(m):
                count += 1
            elif '3' in str(t):
                count += 1
            else:
                pass
print(count)

#위 코드는 모범 답안을 참고하여 작성
#3이 포함되는 것을 체크하는 과정을 string 화 하여 체크하는 것이 포인트

#실전 문제 : 왕실의 나이트
#왕실 정원은 체스판 처럼 8 X 8
#특정 한 칸에 나이트가 위치
#이동할 때 L 자 형태로만 이동하며 정원 밖으로는 나갈 수 없음
#1. 수평으로 두 칸 이동한 뒤 수직으로 한 칸 이동
#2. 수직으로 두 칸 이동한 뒤 수평으로 한칸 이동

#첫째 줄에 8 X 8 평면 상에 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력
#표현 방식은 열 : a ~ h / 행 : 1 ~ 8 순으로 이루어 짐

#출력 조건 : 첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력

#이슈 : 영어를 입력할 시 이를 어떻게 좌표 처리할 것인가.. 바로 안떠오름
print('나이트의 위치를 입력')
loc = [0] * 2
loc = list(map(str, input()))

word = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

#영문숫자로 주어진 좌표를 숫자 순서쌍 표현으로 다음과 같이 변경해봄
for i in range(len(word)):
    if word[i] == loc[0]:
        loc[0] = i+1

loc[1] = int(loc[1])

count = 0
for i in range(2):
    for j in [-1, 1]:
        loc_first = loc[i] + 2*j
        if loc_first < 1 or loc_first > 8:
            pass
        else:
            for k in [-1, 1]:
                loc_second = loc[1-i] + 1*k
                if loc_second >= 1 and loc_second <=8:
                    count += 1
                else:
                    pass
print(count)
#자체 평가 : 조건문이 꽤나 들어가서 실수하기 쉬울 듯 / 특히나 영문숫자 입력을 어떻게 처리할지 고민을 많이 함
#모범 답안에선 이동가능한 좌표 방향을 정의하고 이를 따로 Set 처리

#실전 문제 : 게임 개발
#게임 캐릭터가 맵 안에서 움직이는 시스템을 개발
#장소는 1 X 1 크기의 정사각형으로 이루어진 N X M 크기의 직사각형
#각각의 칸은 육지 또는 바다
#캐릭터는 동 / 서 / 남 / 북 한 곳을 바라봄
#각 칸은 (A, B) A : 북쪽으로 떨어진 칸의 개수 / B : 서쪽으로부터 떨어진 칸의 개수
#상하좌우로 움직일 수 있고 바다로는 갈 수 없음
#1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례로 갈 곳을 정함
#2. 캐릭터의 바로 왼쪽 방향에 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸 전진. 가보지 않은 칸이 없다면 왼쪽 방향으로 회전만 수행하고 1단계로 돌아감
#3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아감. 단, 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춤

#첫째 줄에 맵의 사이즈 N, M을 공백으로 구분하여 입력(3이상 50이하)
#둘째 줄에 게임 캐릭터가 있는 좌표 (A, B)와 바라보는 방향 d가 각각 서로 공백으로 구분하여 주어짐
#방향 d의 값은 0 : 북쪽 / 1 : 동쪽 / 2 : 남쪽 / 3 : 서쪽
#셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어짐.
#각 줄의 데이터는 북쪽에서 남쪽 순으로 주어짐
#0 : 육지 / 1 : 바다 / 맵의 외곽 또한 바다
#게임 캐릭터의 첫 위치는 항상 육지

#출력 조건 : 첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력

print('장소 사이즈 N X M 결정')
N, M = map(int, input().split())

print('캐릭터의 위치 (A, B) / 캐릭터의 시선 결정')
A, B, d = map(int, input().split())

chr_sta = [A, B, d]

print('장소 커스텀 육지 / 바다')
world = [[0]*M for _ in range(N)]
for i in range(N):
    world[i] = list(map(int, input().split()))

#가본 곳을 지정하는 방법? 리스트를 만들어서 처리
mark = []
mark.append([A, B]) #시작 지점도 가본 곳

#왼쪽 방향처리? 예를 들어 현재 시선이 북쪽이면 서쪽을 처리
#0 > 3 > 2 > 1 > 0
def direction(a):
    a[2] -= 1
    if a[2] == -1:
        a[2] = 3

A = chr_sta[0]
B = chr_sta[1]
stop = 0

while stop == 0:
    if chr_sta[2] == 1:
        direction(chr_sta)
        B -= 1
        if [A, B] not in mark and B > 0 and world[A-1][B-1] == 0:
            mark.append([A, B])
            chr_sta[1] -= 1
        else:
            pass
    elif chr_sta[2] == 0:
        direction(chr_sta)
        A -= 1
        if [A, B] not in mark and A > 0 and world[A-1][B-1] == 0:
            mark.append([A, B])
            chr_sta[0] -= 1
        else:
            pass
    elif chr_sta[2] == 3:
        direction(chr_sta)
        B += 1
        if [A, B] not in mark and B < 9 and world[A-1][B-1] == 0:
            mark.append([A, B])
            chr_sta[1] += 1
        else:
            pass
    elif chr_sta[2] == 2:
        direction(chr_sta)
        A += 1
        if [A, B] not in mark and A < 9 and world[A-1][B-1] == 0:
            mark.append([A, B])
            chr_sta[0] += 1
        else:
            pass
    elif [chr_sta[0]+1, chr_sta[1]] in mark and [chr_sta[0]-1, chr_sta[1]] in mark and [chr_sta[0], chr_sta[1]+1] in mark and [chr_sta[0], chr_sta[1]-1] in mark:
        if chr_sta[2] == 3:
            chr_sta[0] += 1
            if world[chr_sta[0]][chr_sta[1]] == 1 or chr_sta[0] > 8:
                stop += 1
        elif chr_sta[2] == 2:
            chr_sta[1] -= 1
            if world[chr_sta[0]][chr_sta[1]] == 1 or chr_sta[1] < 1:
                stop += 1
        elif chr_sta[2] == 1:
            chr_sta[0] -= 1
            if world[chr_sta[0]][chr_sta[1]] == 1 or chr_sta[0] < 1:
                stop += 1
        elif chr_sta[2] == 0:
            chr_sta[1] += 1
            if world[chr_sta[0]][chr_sta[1]] == 1 or chr_sta[1] > 8:
                stop += 1
        else:
            pass    

print(len(mark))




