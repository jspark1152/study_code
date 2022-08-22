'''
한울이가 사는 나라에는 N개의 여행지(1~N번)
임의의 두 여행지 사이에는 두 여행지를 연결하는 도로가 존재(양방향)
한울이가 계획한 여행 계획이 가능한지 여부 파악

입력 조건
1. 첫줄에 여행지 수 N, 여행 계획에 속한 도시의 수 M 입력
2. N개의 줄에 걸쳐 N X N 행렬 형태로 두 여행지가 서로 연결되어 있는지 여부가 주어짐
3. 마지막 줄에 한울이의 여행 계획에 포함된 여행지의 번호들이 주어짐

출력 조건 : 여행 계획이 가능하면 YES, 아닐 경우 NO 출력
'''

print('여행지 수 N, 여행 계획에 속한 도시 수 M 입력')
N, M = map(int, input().split())

route = []
print('여행지 연결 정보 입력')
for _ in range(N):
    route.append(list(map(int, input().split())))


print('여행 계획 입력')
plan = list(map(int, input().split()))

inf = int(1e9)
for m in range(N):
    for n in range(N):
        if route[m][n] == 0:
            route[m][n] = inf

for k in range(N):
    for i in range(N):
        for j in range(N):
            route[i][j] = min(route[i][j], route[i][k]+route[k][j])

result = 0
for i in range(1, M):
    if route[plan[0]][i] == inf:
        result += 1 #그 도시로의 여행이 불가능하다는 것
        break

if result == 0:
    print('YES')
else:
    print('NO')

#자체 평가 : 음.. 어쨋건 통로가 모두 이어져야한다는 점. 즉, 출발 도시에서 모든 도시가 어떻게든 연결이 되어 있어야 함. 최단 경로 알고리즘으로 구현해봤음.