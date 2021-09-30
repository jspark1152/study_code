#실전 문제 : 미래 도시
#판매원 A는 현재 1번 회사에 위치
#1 ~ N번까지 회사가 존재하는데 이 중 X번 회사에 방문해야함
#특정 회사끼리 서로 도로를 통해 연결되어 있으며 이는 쌍방향 이동이 가능
#또한 이동하는 비용은 1로 동일
#판매원 A는 소개팅 상대를 만나기 위해 K번 회사에 먼저 방문해야함
#따라서 K번 회사를 방문한 후 X번 회사로 향해야 함

#첫 줄에 전체 회사 개수 N과 경로 수 M을 공백으로 구분하여 입력
#둘째 줄부터 M+1번째 줄에는 연결된 두 회사 번호가 공백으로 구분되어 주어짐
#M+2번째 줄에는 X와 K가 공백으로 구분되어 차례로 주어짐

#출력 조건 : 첫 줄에 K번 회사를 거쳐 X번 회사로 가는 최소 이동 시간을 출력
#단 X번 회사에 도달할 수 없는 경우 -1 출력

print('회사 개수 N과 도로 개수 M을 입력')
N, M = map(int, input().split())

edge = []
print('도로 정보 입력')
for i in range(M):
    a, b = map(int, input().split())
    edge.append((a, b))

print('X와 K를 입력')
X, K = map(int, input().split())

print(edge)

INF = int(1e9)

graph0 = [[] for _ in range(N+2)]

for i in range(M):
    a, b = edge[i][0], edge[i][1]
    graph0[a].append([b, 1])
    graph0[b].append([a, 1])

print(graph0)

graph = graph0

mark0 = [False] * (N+1)

mark = mark0

dist0 = [INF] * (N+1)

dist = dist0

mark[0] = True
dist[1] = 0

def dijkstra(n):
    mark[n] = True
    for i in graph[n]:
        dist[i[0]] = min(dist[i[0]], dist[n] + i[1])

def sel_min():
    a = 0
    for i in range(1, N+1):
        if mark[i] == True:
            pass
        else:
            if dist[i] < dist[a]:
                a = i
    return a

graph[X]=[]

for i in range(N+1):
    a = sel_min()

    dijkstra(a)
print(dist)
k = dist[K]

graph = graph0
mark = mark0
dist = dist0

mark[K] = True
dist[K] = 0

for i in range(N+1):
    a = sel_min()

    dijkstra(a)
print(dist)
x = dist[X]

if k >= 1e9 or x >= 1e9:
    print(-1)
else:
    print(k+x)

#자체 평가 : 반례가 있을까?
#K번 회사까지의 최단 경로(최소 경비)를 우선 다익스트라로 계산(이 때 X번 회사는 제외)
#X번 회사 제외 아이디어는 경로 그래프에서 X번에서 출발하는 경우를 제외
#그 다음 K번에서 출발하여 X번 까지의 최단 경로를 다익스트라로 계산한 후 합산

#솔루션에서는 이 문제가 플로이드 워셜의 대표적 유형이라고 함
#내가 한 풀이는 두번 계산
#플로이드 워셜 알고리즘 이용시 한번에 두개 계산이 가능

#K번 회사를 가기전 X번 회사를 거칠 수 있느냐?
#거칠 수 없다면 교재의 솔루션은 오답
#문제에서 X에 방문 = 판매라는 문구는 안보이긴 하지만 혼동있을 수 있음

#반례
#X=2, K=3
#(1,2), (2,3)
#이 경우 1번 회사에서 K번 회사까지 가기 위해서는 무조건 X를 거쳐야함

#이 경우 내가 작성한 코드가 맞음