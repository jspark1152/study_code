print('노드 n 간선 m')
n, m = map(int, input().split())
start = int(input())
graph = []

print('간선 정보 입력')
for i in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))



inf = int(1e9)

cost = [inf] * (n+1)

cost[start] = 0
visited = [False] * (n+1)

def dijkstra(start):
    visited[start] = True
    for i in graph:
        if i[0] == start:
            cost[i[1]] = min(cost[i[1]], cost[start]+i[2])
    
    start = 0
    for i in range(1, n+1):
        if cost[i] < cost[start] and not visited[i]:
            start = i
        
    if start == 0:
        return
    else:
        dijkstra(start)

dijkstra(start)

print(cost)