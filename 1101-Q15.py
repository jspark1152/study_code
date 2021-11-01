#특정 거리 도시 찾기
#1 ~ N번까지 도시와 M개의 단방향 도로가 존재
#모든 도로 거리는 1
#이 때 특정 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중 최단 거리가 정확히 K인 모든 도시를 출력하는 프로그램 작성

#입력 조건
#1. 첫 줄에 도시 개수 N, 도로 개수 M, 거리 정보 K, 출발 도시 X 입력
#2. 다음 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B 입력(A도시에서 B도시로 이동하는 도로를 의미)

#출력 조건 : X로부터 출발하여 도달할 수 있는 도시 중 최단 거리가 K인 모든 도시 번호를 한 줄에 하나씩 입력
#단, 존재하지 않으면 -1 출력

print('도시 개수 N, 도로 개수 M, 거리 정보 K, 출발 도시 X 입력')
N, M, K, X = map(int, input().split())

node = []
print('도로 정보 입력')
for i in range(M):
    A, B = map(int, input().split())
    node.append((A, B))

inf = int(1e9)
graph = [[inf]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    graph[i][i] = 0

#도로 정보 입력
for x in node:
    graph[x[0]][x[1]] = 1

#플루이드 워셜 알고리즘
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            graph[i][k] = min(graph[i][k], graph[i][j]+graph[j][k])

#최단거리가 K인 도시 출력
for i in range(1, N+1):
    if graph[X][i] == K:
        print(i)

#존재하지 않는 경우
if K not in graph[X]:
    print(-1)

#자체 평가 : 역시 알고리즘 공부한 효과가 있음. 대표적인 알고리즘 패턴은 반복적으로 구현해보는 것이 필요한 듯 함.