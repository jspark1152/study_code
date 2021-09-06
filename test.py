print('미로 사이즈 결정')
N, M = map(int, input().split())

graph = []
print('미로 정보 입력')
for i in range(N):
    graph.append(list(map(int, input())))

from collections import deque

mark = deque()
mark1 = deque()

def bfs(x, y, visited, graph):
    global count
    
    if graph[x][y] == 1 and visited[x][y] == False:
        mark.append([x, y])
        visited[x][y] = True

    while [N-1, M-1] not in mark:
        for i in range(len(mark)):
            a = mark.popleft()
            
            if a[0]+1 < N:
                if graph[a[0]+1][a[1]] == 1 and visited[a[0]+1][a[1]] == False:
                    mark1.append([a[0]+1, a[1]])
                    visited[a[0]+1][a[1]] = True

            if a[0]-1 >= 0:
                if graph[a[0]-1][a[1]] == 1 and visited[a[0]-1][a[1]] == False:
                    mark1.append([a[0]-1, a[1]])
                    visited[a[0]-1][a[1]] = True

            if a[1]+1 < M:
                if graph[a[0]][a[1]+1] == 1 and visited[a[0]][a[1]+1] == False:
                    mark1.append([a[0], a[1]+1])
                    visited[a[0]][a[1]+1] = True

            if a[1]-1 >= 0:
                if graph[a[0]][a[1]-1] == 1 and visited[a[0]][a[1]-1] == False:
                    mark1.append([a[0], a[1]-1])
                    visited[a[0]][a[1]-1] = True
            
        for j in range(len(mark1)):
            b = mark1.popleft()
            mark.append(b)
        
        count += 1
    
    count += 1 #마지막 칸 추가
        

count = 0
visited = [[False]*M for _ in range(N)]

bfs(0, 0, visited, graph)

print(count)
        
