print('노드 n 간선 m')
n, m = map(int, input().split())

inf = int(1e9)

graph = []
dist = [[inf]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

for i in range(1, n+1):
    dist[i][i] = 0

for i in graph:
    dist[i[0]][i[1]] = i[2]

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

print(dist)