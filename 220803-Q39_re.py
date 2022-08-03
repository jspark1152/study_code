import heapq

print('케이스 수 T 입력')
T = int(input())

inf = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = []
for _ in range(T):
    print('공간 크기 N 및 비용 정보 입력')
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    
    distance = [[inf]*N for _ in range(N)] #최단 비용 맵
    q = [(graph[0][0], 0, 0)] #큐 정의
    distance[0][0] = graph[0][0] #시작점 지정
    
    while q:
        dist, x, y = heapq.heappop(q)
        
        if distance[x][y] < dist:
            continue
        
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            
            if mx < 0 or mx >= N or my < 0 or my >= N:
                continue
            
            cost = dist + graph[mx][my]
            
            if distance[mx][my] > cost:
                distance[mx][my] = cost
                heapq.heappush(q, (cost, mx, my)) #갱신된 포인트 다시 큐 삽입
    
    result.append(distance[N-1][N-1])

for i in range(len(result)):
    print(result[i])