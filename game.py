print('장소 사이즈 N X M 결정')
N, M = map(int, input().split())

print('캐릭터의 위치 (A, B) / 캐릭터의 시선 결정')
A, B, d = map(int, input().split())

print('장소 커스텀 육지 / 바다')
world = [[0]*M for _ in range(N)]
for i in range(N):
    world[i] = list(map(int, input().split()))

#가본 곳을 지정하는 방법? 리스트를 만들어서 처리
mark = []
mark.append([A, B]) #시작 지점도 가본 곳

print(mark)

#순서
#1. 갈 곳이 육지인지
#2. 갈 곳이 처음 가는 곳인지
#3. 앞으로 이동 여부 결정
#4. 앞으로 이동 못하는 경우 뒤로 이동할 수 있는지 여부 결정

#1st issue : xy평면 좌표로 착각
#2nd issue : 함수 정의시 global 변수 놓침

#육지인지 체크
def check_left(A, B, d):
    if d == 0:
        if B-1 >= 0 and world[A][B-1] == 0:
            return 0 #0은 육지를 의미
        else:
            return 1 #1은 바다를 의미
    elif d == 3:
        if A+1 <= N-1 and world[A+1][B] == 0:
            return 0
        else:
            return 1
    elif d == 2:
        if B+1 <= M-1 and world[A][B+1] == 0:
            return 0
        else:
            return 1
    elif d == 1:
        if A-1 >= 0 and world[A-1][B] == 0:
            return 0
        else:
            return 1

#뒤로 이동시 바다인지 여부
def check_back(A, B, d):
    if d == 0:
        if A+1 > N-1 or world[A+1][B] == 1:
            return 1 #1은 바다를 의미
        else:
            return 0 #0은 육지를 의미
    elif d == 3:
        if B+1 > M-1 or world[A][B+1] == 1:
            return 1
        else:
            return 0
    elif d == 2:
        if A-1 < 0 or world[A-1][B] == 1:
            return 1
        else:
            return 0
    elif d == 1:
        if B-1 < 0 or world[A][B-1] == 1:
            return 1
        else:
            return 0

#갔었던 장소인지 확인
def check_first(A, B, d):
    if d == 0:
        if [A, B-1] not in mark:
            return 0 #0은 가본 적 없는 곳
        else:
            return 1 #1은 가본 적 있는 곳
    elif d == 3:
        if [A+1, B] not in mark:
            return 0
        else:
            return 1
    elif d == 2:
        if [A, B+1] not in mark:
            return 0
        else:
            return 1
    elif d == 1:
        if [A-1, B] not in mark:
            return 0
        else:
            return 1

#왼쪽 방향처리? 예를 들어 현재 시선이 북쪽이면 서쪽을 처리
#0 > 3 > 2 > 1 > 0
def rot_left():
    global d
    d -= 1
    if d == -1:
        d = 3

def move_for(d):
    global A, B
    if d == 0:
        A -= 1
    elif d == 3:
        B -= 1
    elif d == 2:
        A += 1
    elif d == 1:
        B += 1

def move_back(d):
    global A, B
    if d == 0:
        A += 1
    elif d == 3:
        B += 1
    elif d == 2:
        A -= 1
    elif d == 1:
        B -= 1

turn = 0

while True:
    while turn != 4:
        if check_left(A, B, d) == 0 and check_first(A, B, d) == 0:
            rot_left()
            move_for(d)
            mark.append([A, B])
            turn = 0
            print(d)
        elif check_left(A, B, d) == 0 and check_first(A, B, d) == 1:
            rot_left()
            turn += 1
            print(d)
        elif check_left(A, B, d) == 1:
            rot_left()
            turn += 1
            print(d)
        else:
            pass

    move_back(d)

    if world[A][B] == 0:
        turn = 0
    else:
        break
    
 
print(mark)
print(len(mark))



