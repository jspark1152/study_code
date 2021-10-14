import heapq

print('노드 n 간선 m')
n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]

print('간선 정보 입력')
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

inf = int(1e9)

distance = [inf] * (n+1)

def dijkstra_q(start):
    q=[]

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        print(q)
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra_q(start)

print(distance)