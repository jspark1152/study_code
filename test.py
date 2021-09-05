print('미로 사이즈 결정')
N, M = map(int, input().split())

graph = []
print('미로 정보 입력')
for i in range(N):
    graph.append(list(map(int, input())))

from collections import deque

mark = deque()

def end():
    global k
    k += 1

def bfs(x, y, visited, graph):
    global k
    if x<=-1 or x>=N or y<=-1 or y>=M:
        return False
    
    if graph[x][y]==1 and visited[x][y]==False:
        mark.append([x, y])
        print(mark)
        visited[x][y] = True
    else:
        return False

    if [N-1, M-1] in mark:
        end()

    a = mark.popleft()

    if a != [N-1, M-1]:
        k += 1
        bfs(a[0]+1, a[1], visited, graph)
        bfs(a[0]-1, a[1], visited, graph)
        bfs(a[0], a[1]+1, visited, graph)
        bfs(a[0], a[1]-1, visited, graph)
    return False

visited=[[False]*M for _ in range(N)]

k=0
bfs(0, 0, visited, graph)

print(k)