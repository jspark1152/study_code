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
        
        #gas 퍼트리기

for emp in sel_empty:
    lab_0 = block_gas(emp)
    print(lab_0)

    