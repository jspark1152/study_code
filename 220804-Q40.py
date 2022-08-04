'''
40. 숨바꼭질
1 ~ N 개의 헛간 존재
술래는 1번에서 출발
M 개의 양방향 통로가 존재하여 서로 다른 두 헛간을 연결
1번 헛간으로부터 최단 거리가 가장 먼 헛간이 가장 안전

입력 조건
1. 첫 줄에 N(2이상 20,000이하), M(1이상 50,000이하) 입력
2. M개의 줄에 걸쳐 통로 정보 입력

출력 조건 : 숨어야 하는 헛간(동일 거리인 경우 번호가 작은 헛간), 그 헛간까지의 거리, 그 헛간과 같은 거리인 헛간의 개수
'''

print('헛간 개수 N 과 통로 개수 M 입력')
N, M = map(int, input().split())

inf = int(1e9)
graph = [[inf]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    graph[i][i] = 0

print('통로 정보 입력')
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
#주어진 통로 정보를 통해 기본 거리 정보 입력 > 이후 최단 거리 계산하면 될듯

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
            
print(graph)

#출력 조건 생각보다 까다롭네. 최단 거리가 가장 큰 거리 값부터 찾고 그 거리로부터 나머지 값을 탐색.
result_max = 0
for i in range(2, N+1):
    result_max = max(result_max, graph[1][i])

result_list = []
for i in range(2, N+1):
    if graph[1][i] == result_max:
        result_list.append(i)

print(result_list[0], result_max, len(result_list))

#자체 평가 : 모범 답안에는 다익스트라로 풀이했네;; 음..