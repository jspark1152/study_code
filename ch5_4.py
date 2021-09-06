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
mark1 = deque()

def bfs(x, y, visited, graph):
    global count
    
    if graph[x][y] == 1 and visited[x][y] == False:
        mark.append([x, y])
        visited[x][y] = True

    while [N-1, M-1] not in mark: #최종점이 mark에 포함되는 순간 종료
        for i in range(len(mark)): #mark 원소 개수만큼 반복
            a = mark.popleft() #맨 앞 원소 추출하여 이 원소 상하좌우를 확인
            
            if a[0]+1 < N: #왜 굳이 이렇게 조건을.. 아래 if문과 함께 하니 list range 벗어나는 오류 발생;; 왜지?
                if graph[a[0]+1][a[1]] == 1 and visited[a[0]+1][a[1]] == False:
                    mark1.append([a[0]+1, a[1]]) #바로 mark에 삽입이 불가능하기 때문에 mark1에 삽입
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
            
        for j in range(len(mark1)): #mark1에 들어간 데이터를 그대로 mark에 삽입과 동시에 mark1은 빈 list로 초기화
            b = mark1.popleft()
            mark.append(b)
        
        count += 1 #모든 사이클에 대한 횟수 증가
    
    count += 1 #마지막 칸 추가
        

count = 0
visited = [[False]*M for _ in range(N)]

bfs(0, 0, visited, graph)

print(count)

#자체 평가 : 해냈음. 동시 다발적으로 이동해가는 것에 포인트를 두고 구현.
#후련함. 여러 경우를 모두 대입해봐도 정답 출력. Good.
#알고리즘 사고 방식이 낯설어서 아직 어려움이 있음