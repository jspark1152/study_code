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
bus = []
print('버스 정보 입력')
for i in range(m):
    l = list(map(int, input().split())) #와 너무 안햇나 이거 기억이 안나네 ㅋㅋㅋ
    bus.append(l)

print(bus)

map = [[0]*n for i in range(n)]

print(map)

for i in bus:
    map[i[0]-1][i[1]-1] = i[2]

print(map)