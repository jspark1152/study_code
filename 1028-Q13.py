#치킨 배달
#크기가 N X N 인 도시 (1 X 1 칸으로 나누어져 있음)
#도시의 각 칸은 빈칸0, 치킨집1, 집2 중 하나
#도시의 칸은 (r, c)로 나타냄
#치킨 거리 : 집과 가장 가까운 치킨집 사이의 거리
#각각의 집은 치킨 거리를 가짐
#도시의 치킨 거리 : 모든 집의 치킨 거리의 합
#이 때 치킨집을 최대 M개를 고르고 나머지 치킨집은 모두 폐업
#치킨집을 어떻게 선택해야 도시의 치킨 거리가 가장 작게 될지

#입력 조건
#1. 첫줄에 N과 M이 주어짐
#2. 둘째 줄부터 N개의 줄에 도시의 정보 입력

#출력 조건 : 치킨집을 최대 M개 선택했을 때 도시 치킨 거리의 최솟값 출력

print('도시 크기 N, 치킨집 개수 M 입력')
N, M = map(int, input().split())

city = []
print('도시 정보 입력')
for i in range(N):
    a = list(map(int, input().split()))
    city.append(a)
print(city)

house = []
chicken = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            chicken.append((i, j))
        elif city[i][j] == 2:
            house.append((i, j))

print(house)
print(chicken)

#치킨집 M개 선택 경우의 수
from itertools import combinations
sel_chic = list(combinations(chicken, M))
print(sel_chic)

#'치킨 거리' 계산
def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

#선별된 치킨집에 대한 '도시의 치킨 거리' 계산
def min_dist(sel):
    dist = 0
    for h in house:
        k = int(1e9)
        for i in sel:
            d = distance(h, i)
            if d <= k:
                k = d
        dist += k
    return dist                   

#치킨집 M개의 모든 경우에 대한 도시의 치킨 거리 중 최솟값
result = int(1e9)
for sel in sel_chic:
    dist = min_dist(sel)
    if dist <= result:
        result = dist

print(result)

#자체 평가 : 치킨집 M개 선택에서 막혔음 > 조합으로 해결해봄(사실 처음에 떠오른 방법이었는데 다른 방법이 없나 고민)
#다행히 조합으로 구현하는 중에 문제는 특별히 없었음
#솔루션에서도 조합을 이용했군..