#다익스트라 알고리즘은 한 지점에서 다른 특정 지점까지의 최단 경로를 구해야 하는 경우 사용
#플로이드 워셜 알고리즘(Floyd-Warshall Alg.)은 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우에 사용

#n은 노드 / m은 간선
n, m = map(int, input().split())

node_map = [[] for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    node_map[a].append((b,c))

INF = int(1e9)

graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for i in range(1, n+1):
    for (b, c) in node_map[i]:
        graph[i][b] = c

print(graph)

#핵심 i 행과 열을 제외하는 아이디어
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if j != i and k != i:
                graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])

print(graph)

#자체 평가 : 와.. 아이디어 구현 성공.. 어렵지 않았음..