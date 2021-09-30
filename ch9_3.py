#실전 문제 : 전보
#어떤 나라에는 N개의 도시
#각 도시는 다른 도시로 전보를 통해 메시지를 전달
#X도시에서 Y도시로 전보를 보내고자 하면 X에서 Y로의 통로가 설치되어야 함
#X에서 Y로의 통로는 있지만 Y에서 X로의 통로가 없다면 Y는 X로 전보 불가
#통로를 거쳐 메시지를 보낼 때는 일정 시간이 소요
#어느 날 C도시에서 위급 상황이 발생
#최대한 많은 도시로 메시지를 보내고자 함
#메시지는 C도시에서 출발하여 각 도시 사이에 설치된 통로를 거쳐 최대한 많이 퍼져나감
#각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때 도시 C에서 보낸 메시지를 받게 되는 도시의 개수는 총 몇 개이며 도시들이 모두 메시지를 받는데 걸리는 시간은 얼마인지

#첫 줄에 도시 개수 N, 통로 개수 M, 메시지를 보내고자 하는 도시 C
#1<=N<=30,000  1<=M<=200,000  1<=C<=N
#둘째 줄부터 M+1번째 줄에 걸쳐서 통로에 대한 정보 X, Y, Z가 주어짐
#X에서 Y로의 통로, 메시지가 전달되는 시간이 Z

#출력 조건 : 첫 줄에 도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간을 공백으로 구분하여 출력

print('도시 개수 N, 통로 수 M, 메시지 보내는 C도시 입력')
N, M, C = map(int, input().split())

graph = [[] for _ in range(N+1)]
print('통로 정보 입력')
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

INF = int(1e9)

mark = [False] * (N+1)

dist = [INF] * (N+1)

def dijkstra(n):
    mark[n] = True

    for i in graph[n]:
        dist[i[0]] = min(dist[i[0]], dist[n]+i[1])

def sel_min():
    a = 0
    for i in range(1, N+1):
        if not mark[i]:
            if dist[i] < dist[a]:
                a = i
    return a

dist[C] = 0

for _ in range(N):
    n = sel_min()

    dijkstra(n)

print(dist)

count = 0
cost = 0
for i in range(1, N+1):
    if dist[i] != 0 and dist[i] < INF:
        count += 1
    if dist[i] > cost:
        cost = dist[i]

print(count, cost)

#자체 평가 : 다익스트라 알고리즘으로 구현
#다만 데이터 사이즈가 클 경우;; 큐로 구현했어야 하는데 아직 익숙치가 않음