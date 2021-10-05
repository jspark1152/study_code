from collections import deque

print('노드 N, 간선 M')
N, M = map(int, input().split())

graph = []

print('간선 정보 입력 a 에서 b')
for i in range(M):
    a, b = map(int, input().split())
    graph.append((a, b))

print(graph)

#진입 차수 계산
deg = [0] * (N+1)

for i in graph:
    deg[i[1]] += 1

visited = [0] * (N+1)

def deg_zero(deg):
    zero = []
    for i in range(1, N+1):
        if deg[i] == 0 and visited[i] == 0:
            zero.append(i)
    return zero

def top_sort(n):
    for i in graph:
        if i[0] == n:
            graph.remove(i)

q = deque()
map = []

zero = []
for i in range(1, N+1):
    if deg[i] == 0 and visited[i] == 0:
        zero.append(i)

for i in zero:
    q.append(i)

print(q)

while q:
    n = q.popleft()
    visited[n] = 1
    map.append(n)
    for i in graph:
        if i[0] == n:
            graph.remove(i)
    deg = [0] * (N+1)
    zero = []
    for i in range(1, N+1):
        if deg[i] == 0 and visited[i] == 0:
            zero.append(i)
    for i in zero:
        q.append(i)

print(map)
