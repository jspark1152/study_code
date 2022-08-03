print('학생 수 N 및 성적 비교 횟수 M 입력')
N, M = map(int, input().split())

inf = int(1e9)
graph = [[inf]*(N+1) for _ in range(N+1)]

print('성적 비교 자료 A < B 입력')
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 0

for i in range(1, N+1):
    graph[i][i] = 0

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

print(graph)

result = []
for i in range(1, N+1):
    pt = 0
    for j in range(1, N+1):
        if graph[i][j] == 0 or graph[j][i] == 0:
            pt += 1
    if pt == N:
        result.append(i)

print(result)
print(len(result))