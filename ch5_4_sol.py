from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = deque()
    queue.append([x, y]) #x,y는 좌표 값으로 변하지 않는 값이기 때문에 tuple처리해도 됨

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            if x+dx[i]<=-1 or x+dx[i]>=N or y+dy[i]<=-1 or y+dy[i]>=M:
                continue

            if graph[x+dx[i]][y+dy[i]] == 1: #이 표현 유용하게 쓰일듯 기억해두자
                continue

            if graph[x+dx[i]][y+dy[i]] == 1:
                graph[x+dx[i]][y+dy[i]] = 1 + graph[x][y]
                queue.append([x+dx[i], y+dy[i]])
        
        if [N-1, M-1] in queue:
            while queue:
                queue.popleft()
    

bfs(0, 0)

print(graph[N-1][M-1])

#모범 답안에서는 거쳐가는 포인트에 그대로 값을 누적 > 최종점 도달시 종료 > 최종점의 누적값 출력
            
