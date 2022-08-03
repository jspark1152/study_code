print('도시 수 n 입력')
n = int(input())

print('버스 개수 m 입력')
m = int(input())

inf = int(1e9)
graph = [[inf]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

print('버스 운영 정보 입력')
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

'''
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == inf:
            graph[i][j] = 0
print(graph)
for i in range(1, n+1):
    print(graph[i][1:], end = '')
''' 

#신기하네 이런 print 출력 방법도 있네
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == inf:
            print(0, end = ' ') #' ' 공백 추가하면 띄어쓰기 가능
        else:
            print(graph[i][j], end = ' ')
    print()