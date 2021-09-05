#실전 문제 3. 음료수 얼려 먹기
#N X M 얼음 틀이 있음
#구멍이 난 곳은 0, 칸막이가 존재하는 부분은 1로 표시
#0이 상하좌우로 붙은 경우 연결된 것으로 간주
#이때 얼음 틀 모양이 주어졌을 때 생성되는 총 얼음의 개수

#1. 첫 번째 줄에 얼음 틀의 세로길이 N과 가로길이 M이 주어짐(1이상 1,000이하)
#2. 두 번째 줄부터 N+1번째 줄까지 얼음틀의 형태가 주어짐
#3. 구멍 = 0, 아닌 곳 = 1

#출력 조건 : 한 번에 만들 수 있는 얼음 개수를 출력

print('얼음 케이스 사이즈')
N, M = map(int, input().split())

case = [[0] * M for _ in range(N)]

print('케이스 형태 결정')
for i in range(N):
    case[i] = list(map(int, input().split()))

hole_list = []

for i in range(N):
    for j in range(M):
        if case[i][j] == 0:
            hole_list.append([i, j])

print(hole_list)

node = [[] for _ in range(N*M)]
stack = []
mark = []

def make_node(a):
    while stack:
        if a not in node[n]:
            node[n].append(a)

        k = stack[-1]

        if [k[0]+1, k[1]] in hole_list and [k[0]+1, k[1]] not in mark:
            stack.append([k[0]+1, k[1]])
            mark.append([k[0]+1, k[1]])
            make_node([k[0]+1, k[1]])
        elif [k[0]-1, k[1]] in hole_list and [k[0]-1, k[1]] not in mark:
            stack.append([k[0]-1, k[1]])
            mark.append([k[0]-1, k[1]])
            make_node([k[0]-1, k[1]])    
        elif [k[0], k[1]+1] in hole_list and [k[0], k[1]+1] not in mark:
            stack.append([k[0], k[1]+1])
            mark.append([k[0], k[1]+1])
            make_node([k[0], k[1]+1])
        elif [k[0], k[1]-1] in hole_list and [k[0], k[1]-1] not in mark:
            stack.append([k[0], k[1]-1])
            mark.append([k[0], k[1]-1])
            make_node([k[0], k[1]-1])
        else:
            stack.pop()

n = 0

for i in range(len(hole_list)):
    a = hole_list[i]
    stack.append(a)
    
    if a not in mark:
        mark.append(a)
        make_node(a)

    stack = []
    n += 1

node = [i for i in node if len(i) != 0]

print(node)
print(len(node))

#자체 평가 : 머리속에서 그려진 알고리즘을 구현하는데 너무 어려웠음. 재귀 방식이 낯설어서 그런듯. 계속 오류나고..
#아직 표현 센스가 부족함
