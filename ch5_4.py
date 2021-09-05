#실전 문제 4 : 미로 탈출
#동빈이는 N x M 직사각형 미로에 갇혀 있음
#미로에는 여러 괴물이 있어 이를 피해 탈출
#동빈 위치 = (1, 1) / 출구 = (N, M)
#한 번에 한 칸씩 이동
#괴물의 위치는 0 / 없는 곳은 1
#미로는 반드시 탈출 가능한 형태로 제시
#이때 탈출하기 위해 움직여야 하는 최소 칸의 개수(시작 칸과 마지막 칸 모두 포함)

#첫째 줄에 두 정수 N, M(4 이상 200 이하)이 주어짐
#다음 N개의 줄에 각 M개의 정수로 미로 정보가 입력(공백 없이 입력)
#시작 칸과 마지막 칸은 항상 1

#출력 조건 : 첫 줄에 최소 이동 칸의 개수를 출력

print('미로 사이즈 결정')
N, M = map(int, input().split())

graph = []
print('미로 정보 입력')
for i in range(N):
    graph.append(list(map(int, input())))

from collections import deque

mark = deque()

def bfs(x, y, visited):
    global mark
    global k
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    
    if graph[x][y] == 1 and visited[x][y] == False:
        mark.append([x, y])
        visited[x][y] = True
        print(mark)
       
    else:
        return False

    while [N-1, M-1] not in mark:
            a = mark.popleft()
            k+=1

            bfs(a[0]+1, a[1], visited)
            bfs(a[0], a[1]+1, visited)
            bfs(a[0]-1, a[1], visited)
            bfs(a[0], a[1]-1, visited)
               
k = 0
visited = [[False]*M for _ in range(N)]
bfs(0, 0, visited)

print(k+1)
#자체 평가 : 제대로 한게 맞나? 뭔가 어거지로 구현이 된듯한 느낌
#큐를 이용하여 동시에 1인 곳을 통해 퍼져나간다는 아이디어로
#역시 오류 발생