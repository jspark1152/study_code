#뱀
#Dummy 라는 게임에서는 뱀이 나와서 기어다님
#사과를 먹으면 뱀 길이가 늘어남
#기어다니다가 벽 또는 자기 자신의 몸과 부딪히면 게임이 끝남
#게임은 N X N 정사각 보드 위에서 진행되며 특정 칸에는 사과가 놓여짐
#보드 상하좌우 끝에는 벽이 있음
#시작점은 좌측 상단이며 뱀의 길이는 1
#처음에 뱀은 오른쪽을 향함
#다음 규칙하에 매초마다 이동을 함
#1. 먼저 뱀은 몸길이를 늘려 머리를 다음 칸에 위치
#2. 이동한 칸에 사과가 있다면, 사과가 없어지고 꼬리는 움직이지 않음
#3. 이동한 칸에 사과가 없다면, 몸 길이를 줄여서 꼬리가 위치한 칸을 비워줌
#사과의 위치와 뱀의 이동 경로가 주어질 때 게임이 몇 초에 끝나는지 계산

#입력 조건
#1. 첫 줄에 보드의 크기 N이 주어짐(2이상 100이하)
#2. 다음 줄에 사과의 개수 K가 주어짐(0이상 100이하)
#3. 다음 K줄에 걸쳐 사과의 위치가 주어지는데, (행, 렬) 형태로 주어지며 시작점에는 사과가 존재하지 않음
#4. 다음 줄에는 뱀의 방향 변환 횟수 L이 주어짐(1이상 100이하)
#5. 다음 L개의 줄에는 방향 변환 정보가 주어지는데, X와 C로 이루어짐
#5-1) 게임 시작 후 X초가 끝난 뒤에 C가 L(왼쪽) / D(오른쪽) 주어지며 주어진 C방향으로 90도 회전

#출력 조건 : 게임이 몇초에 끝나는지 출력

print('보드 크기 N 입력')
N = int(input())

print('사과 개수 K 입력')
K = int(input())

apple = []
print('사과 위치 입력')
for i in range(K):
    a, b = map(int, input().split())
    apple.append((a, b))

print('뱀 방향 전환 횟수 K 입력')
K = int(input())

rota = []
print('방향 전환 정보 입력')
for i in range(K):
    c, d = input().split()
    rota.append((int(c), d))

print(apple)
print(rota)

from collections import deque

#뱀을 큐로 구현 [꼬리-----머리] 즉, 이동할 때 머리 위치를 append 하면서 꼬리를 popleft 할 예정
snake = deque()
snake.append((1, 1))

direction = (0, 1)
def rotation(C):
    global direction
    if C == 'L':
        if direction == (0, 1):
            direction = (-1, 0)
        elif direction == (-1, 0):
            direction = (0, -1)            
        elif direction == (0, -1):
            direction = (1, 0)            
        elif direction == (1, 0):
            direction = (0, 1)            
    elif C == 'D':
        if direction == (0, 1):
            direction = (1, 0)            
        elif direction == (1, 0):
            direction = (0, -1)            
        elif direction == (0, -1):
            direction = (-1, 0)            
        elif direction == (-1, 0):
            direction = (0, 1)

sec = 0

stop = 0

C = 0

while stop == 0:
    sec += 1

    head = snake[-1]
    a = head[0] + direction[0]
    b = head[1] + direction[1]
    next = (a, b)
    print(next)
    #몸과 충돌 여부
    if next in snake:
        stop = 1
    else:
        snake.append(next)
    #벽과 충돌 여부
    if next[0] < 1 or next[0] > N or next[1] < 1 or next[1] > N:
        stop = 1
    else:
        pass
    #머리 위치 업데이트
    head = snake[-1]
    
    #사과 확인
    if head in apple:
        #사과 제거
        apple.remove(head)
    else:
        #사과가 없기 때문에 꼬리 제거
        snake.popleft()
    print(snake)
    #방향 확인
    #회전이 안되네 왜지?
    #rotation 함수에서 direction 변수를 global로 지정했어야...
    for i in range(len(rota)):
        if sec == rota[i][0]:
            rotation(rota[i][1])

    print(direction)

print(sec)

#자체 평가 : 함수 변수 글로벌화 문제 외엔 크게 문제되는 곳이 없었음. 단, 조금 오래 걸린듯 함.
#뱀 몸통 구현을 큐로 한것이 주효한 듯함.