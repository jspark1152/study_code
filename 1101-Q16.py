#연구소
#연구소에서 바이러스가 유출되어 확산을 막기 위해 연구소에 벽을 세우려고 함
#연구소의 크기는 N X M
#연구소는 빈칸 / 벽으로 구성
#벽은 칸 하나를 차지
#일부 칸은 바이러스가 존재하며 바이러스는 상하좌우 인접한 빈칸으로 퍼질 수 있음
#벽은 꼭 3개를 세울 수 있음
#0 : 빈칸 / 1 : 벽 / 2 : 바이러스
#바이러스가 닿지 않는 영역을 안전 영역이라고 할때 이 영역이 최대가 되게 하는 프로그램 작성

#입력 조건
#1. 연구소 크기 N, M 입력(3이상 8이하)
#2. 다음 줄부터 N개의 줄에 연구소 정보 입력
#3. 2의 개수는 2 이상 10 이하, 0 의 개수는 3개 이상

#출력 조건 : 안전 영역 최대 크기를 출력

print('N, M 입력')
N, M = map(int, input().split())

print('연구소 정보 입력')
lab = []
for i in range(N):
    info = list(map(int, input().split()))
    lab.append(info)

#음.. 아이디어가 안떠오름
#벽을 효율적으로 세우는 아이디어가 필요한데..
#모든 경우 다 따져서? 최소값?

#벽을 3개 세우는 경우부터
empty = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            empty.append((i, j))

from itertools import combinations

sel_empty = list(combinations(empty, 3))
print(len(sel_empty))


#후.. 함수 변수끼리 복제하는데 문제 발생
#생각보다 까다롭네.. 얕은복사/깊은복사;;
import copy

def block_gas(emp):
    #단순히 lab_0 = lab 으로 선언시 두 변수가 동일시(얕은 복사 개념)되는 문제가 발생 ㅡㅡ
    lab_0 = copy.deepcopy(lab)
    lab_0[emp[0][0]][emp[0][1]] = 1
    lab_0[emp[1][0]][emp[1][1]] = 1
    lab_0[emp[2][0]][emp[2][1]] = 1
    return lab_0

#list index out of range : 내가 자주 범하는 실수인데 특히 가정문에서 내가 착각하는것이 없는 값은 확인을 안하겠지라고 생각했던거 같음
#근데 가정 조건문에서도 일단 해당 리스트를 뒤져보기 때문에 반드시 인덱스 맞춰줘야함 
#gas 퍼트리기
def gas(lab_0, i, j):
    if i-1 >= 0:
        if lab_0[i-1][j] == 0:
            lab_0[i-1][j] = 2
            gas(lab_0, i-1, j)

    if j-1 >= 0:
        if lab_0[i][j-1] == 0 and j-1 >= 0:
            lab_0[i][j-1] = 2
            gas(lab_0, i, j-1)

    if i+1 < N:
        if lab_0[i+1][j] == 0 and i+1 < N:
            lab_0[i+1][j] = 2
            gas(lab_0, i+1, j)

    if j+1 < M:
        if lab_0[i][j+1] == 0 and j+1 < M:
            lab_0[i][j+1] = 2
            gas(lab_0, i, j+1)

result = 0

for emp in sel_empty:
    lab_0 = block_gas(emp)
    
    for i in range(N):
        for j in range(M):
            if lab_0[i][j] == 2:
                
                gas(lab_0, i, j)
    print(lab_0)
    count = 0
    for i in range(N):
        for j in range(M):
            if lab_0[i][j] == 0:
                count += 1
    
    result = max(result, count)
    
print(result)

#자체 평가 : 어찌 저찌 구현 성공. 꽤나 오래 걸렸음. 특히 block_gas 함수 작성할 때 copy 개념에서 막혔음.
#그나저나 이게 맞는지..
#모든 경우를 다 뒤져서 그중에 가장 0이 많은 값을 취하는 프로그램인데.. 어려웠다 이건
#음.. 솔루션에서 항상 보면 작성하는 방식이 좀 색다름
#아이디어는 같은데 step 을 좀 더 나누어 짜는듯한 느낌
#와.. 재귀표현을 저렇게 했네.. 답안이라 그런가 신선하다
#재귀표현을 잘하면 뭔가 좀더 코드 자체가 세련돼 보이는 듯함