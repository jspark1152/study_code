#실전 문제 : 커리큘럼
#각 온라인 강의는 선수 강의가 있을 수 있음
#총 N개의 강의를 듣고자 하며 모든 강의는 1번부터 N번까지 번호를 가짐
#동시에 여러 강의 수강 가능
#또한 강의 시간이 강의마다 주어짐
#동빈이가 듣고자 하는 N개의 강의 정보가 주어졌을 때 모두 수강하는데 걸리는 최소 시간 출력
#입력조건
#첫 줄에 듣고자 하는 강의 수 입력(1<=N<=500)
#다음 N개의 줄에 각 강의 시간과 강의를 듣기 위한 선수 강의 번호가 공백으로 구분되어 주어짐
#각 강의 번호는 1부터 N까지로 구성되며 각 줄은 -1로 끝남

#출력 조건 : N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 한 줄에 하나씩 출력

from collections import deque

print('강의 수 N 입력')
N = int(input())

#강의 수강 시간 테이블
time = [0] * (N+1)

#위상 정렬 문제로 보임

inform = [[] for _ in range(N+1)]
#입력시 -1로 마무리.. 해야하는데 이거 어떻게 처리함? 그냥 넣어
for i in range(1, N+1):
    inform[i] = list(map(int, input().split()))
    
print(inform)

#입력 받은 정보로 부터 연결 정보 입력
graph = []
for i in range(1, N+1):
    a = 0
    k = 0
    while a != -1:
        k += 1
        a = inform[i][k]
        if a != -1:
            graph.append((a, i))

print(graph)

q = deque()

visited = [False] * (N+1)

connect = [0] * (N+1)

def zero_con():
    global connect
    connect = [0] * (N+1)
    for i in graph:
        k = i[1]
        connect[k] += 1
    
    for j in range(1, N+1):
        if connect[j] == 0 and not visited[j]:
            q.append(j)
            visited[j] = True

for i in range(1, N+1):
    time[i] = inform[i][0]

zero_con() #q에 시작 포인트 삽입   
print(connect)
print(q)
while q:
    n = q.popleft()
    remove_set = []
    for i in graph:
        if i[0] == n:
            if connect[i[1]] == 1: #시간 중복 합을 막기 위한 조건
                time[i[1]] += time[n]
            remove_set.append(i)
    graph = [i for i in graph if i not in remove_set]
    zero_con()

print(time)

#자체 평가 : 생각보다 까다로웠고 몇 번 오류가 발생하여 수정 반복.
#결과적으로 제대로 된 결과 출력은 하는 듯 함.