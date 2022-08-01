#정말 오랜만인듯. 많이 까먹었겠지? 오히려 리마인드 차원에서 새롭게 접근 가능할지도

'''
n (1 <= n <= 100), 한 도시에서 출발하여 다른 도시에 도착하는 m(1<=m<=100,000)개의 버스
각 버스는 한 번 사용할 때 필요한 비용 존재
모든 도시의 쌍 (A, B) = A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램

입력 조건
1. 첫 줄에 도시 개수 n 입력
2. 둘째 줄에 버스 개수 m 입력
3. 셋째 줄부터 m+2 번째 줄까지 버스 정보 입력 (a, b, c) = (출발도시, 도착도시, 비용)

출력 조건 : n개의 줄 출력(n x n 행렬 형태), (i, j) = i에서 j로 가는 데 필요한 최소 비용
'''

print('도시의 수 n 입력')

n = int(input())

print('버스 수 m 입력')
m = int(input())

INF = int(1e9)
town = [[INF]*(n+1) for i in range(n+1)]
for i in range(1, n+1):
    town[i][i] = 0

print('버스 정보 입력')
for i in range(m):
    a, b, c = map(int, input().split())
    if c < town[a][b]:
        town[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            town[a][b] = min(town[a][b], town[a][k] + town[k][b])

print(town)

for i in range(1, n+1):
    for j in range(1, n+1):
        if town[i][j] == INF:
            town[i][j] = 0

for i in range(1, n+1):
    print(town[i][1:])