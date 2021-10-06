#실전 문제 : 팀 결성
#학교 학생들에게 0 ~ N번까지의 번호를 부여
#처음에는 모든 학생이 서로 다른 팀으로 구분되어 총 N+1개의 팀이 존재
#이 때 선생님은 팀 합치기 연산과 같은 팀 여부 확인 연산을 사용
#1. 팀 합치기 = 두 팀을 합치는 연산
#2. 같은 팀 여부 확인 = 특정한 두 학생이 같은 팀에 속하는지 확인
#선생님이 M개의 연산을 수행할 수 있을 때, 결과를 출력하는 프로그램 작성
#입력 조건
#첫 줄에 N, M이 주어짐(1<=N, M<=100,000)
#다음 M개의 줄에는 각각의 연산이 주어짐
#팀 합치기 연산은 0 a b 형태로 입력. a번이 속한 팀과 b번이 속한 팀을 합친다는 의미
#같은 팀 여부 확인 연산은 1 a b 형태로 입력. a번과 b번 학생이 같은 팀에 속해 있는지를 확인
#a와 b는 N 이하의 자연수

#출력 조건 : 같은 팀 여부 확인 연산에 대하여 한 줄에 하나씩 Yes 혹은 No로 결과 출력

print('번호 N과 연산의 수 M을 입력')
N, M = map(int, input().split())

def find_team(team, x):
    if team[x] != x:
        team[x] = find_team(team, team[x])
    return team[x]

def union_team(team, a, b):
    a = find_team(team, a)
    b = find_team(team, b)
    if a < b:
        team[b] = a
    else:
        team[a] = b

team = [0] * (N+1)

for i in range(N+1):
    team[i] = i

def check_team(a, b):
    a = find_team(team, a)
    b = find_team(team, b)
    if a == b:
        print('Yes')
    else:
        print('No')

graph = []
for i in range(M):
    k, a, b = map(int, input().split())
    graph.append((k, a, b))

for i in graph:
    if i[0] == 0:
        union_team(team, i[1], i[2])
    elif i[0] == 1:
        check_team(i[1], i[2])

#자체평가 : 꽤나 간단했음. 서로소 알고리즘을 알아야만 가능할 듯?