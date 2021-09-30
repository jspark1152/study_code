print('회사 개수 N, 도로 개수 M 입력')
N, M = map(int, input().split())

mark = [False] * (N+1)

INF = int(1e9)

dist = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    dist[i][i] == 0

print('간선 정보 입력')
for i in range(M):
    a, b = map(int, input().split())
    dist[a][b] = 1
    dist[b][a] = 1

print('X, K 입력')
X, K = map(int, input().split())

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

a= dist[1][K]
b= dist[K][X]

if a > int(1e8) or b > int(1e8):
    print(-1)
else:
    print(a+b)

#K번 회사를 가기전 X번 회사를 거칠 수 있느냐?
#거칠 수 없다면 교재의 솔루션은 오답
#문제에서 X에 방문 = 판매라는 문구는 안보이긴 하지만 혼동있을 수 있음

#반례
#X=2, K=3
#(1,2), (2,3)
#이 경우 1번 회사에서 K번 회사까지 가기 위해서는 무조건 X를 거쳐야함
