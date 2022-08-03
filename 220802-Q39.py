'''
39. 화성 탐사
에너지를 효율적으로 사용하고자 출발 지점에서 목표 지점까지 이동할 때 항상 최적의 경로를 찾음
탐사 기계가 존재하는 공간 = N X N
각 칸을 지나기 위한 비용이 존재
가장 왼쪽 위 칸 [0][0] 에서 가장 오른쪽 아래 칸인 [N-1][N-1] 위치로 이동하는 최소 비용을 출력
상하좌우 인접한 곳으로 1칸씩 이동 가능

입력 조건
1. 첫 줄에 테스트 케이스 수 T(1이상 10이하) 입력
2. 매 테스트 케이스의 첫줄에는 공간 크기 N(2이상 125이하)을 입력하고 이어 N줄에 걸쳐 각 칸의 비용이 주어짐

출력 조건 : 최소 비용을 한줄에 하나씩 출력
'''

import heapq

print('테스트 케이스 T 입력')
T = int(input())

#상 / 우 / 하 / 좌
dx = [-1, 0, 1, 0]
dy = [0 , 1, 0, -1]

INF = int(1e9)

result = []
print('공간 크기 N 과 이동 비용 정보 입력')
for _ in range(T):
    N = int(input())
    graph = []
    for _ in range(N):
        l = list(map(int, input().split()))
        graph.append(l)
         
    distance = [[INF]*N for _ in range(N)]
    
    q = [(graph[0][0], 0, 0)]
    distance[0][0] = graph[0][0]
    
    while q:
        dist, x, y = heapq.heappop(q)
        
        if distance[x][y] < dist:
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    result.append(distance[N-1][N-1])
    
for i in range(len(result)):
    print(result[i])
