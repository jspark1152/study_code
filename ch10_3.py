#실전 문제 : 도시 분할 계획
#마을은 N개의 집과 서로 연결하는 M개의 길로 이루어져 있음
#길은 어느 방향으로든지 다닐 수 있는 편리한 길
#길마다 그 길을 유지하는데 필요한 비용이 존재
#마을 이장은 마을을 2개의 분리된 마을로 분할할 계획
#분할 시에는 분리된 마을 안에 집들이 서로 연결되도록 분할
#각 분리된 마을 안에 있는 임의의 두 집 사이에 경로가 항상 존재해야 함
#또한 마을에는 집이 하나 이상
#분리된 두 마을 사이에 있는 길들은 필요가 없으므로 없앨 수 있음
#마을 내에서도 임의의 두집 사이에 경로가 항상 존재하게만 유지시키면서 길을 더 없앨 수 있음
#길의 유지비 합을 최소로 하고 싶어함
#입력조건
#첫줄에 집 개수 N, 길 개수 M이 주어짐. 1<=N<=100,000 / 1<=M<=1,000,000
#그 다음 줄부터 M줄에 걸쳐 길의 정보가 A, B, C 3개의 정수로 공백으로 구분되어 주어짐
#A와 B를 연결하는 길 / 유지비 C

#출력 조건 : 최종 남은 길의 유지비 합의 최솟값 출력

#음 일단 최소 경비 알고리즘(사이클 개념도 포함)
#일단 마을 전체를 계산한 뒤 나누어야하나?(즉 최종 경로들 중 유지비가 가장 많이 드는 경로를 제거 함으로서 분리)

print('집 개수 N, 길 개수 M 입력')
N, M = map(int, input().split())

graph = []
print('길 정보 입력 A, B, C')
for i in range(M):
    A, B, C = map(int, input().split())
    graph.append((A, B, C))

#비용 순으로 오름차순 정렬
graph.sort(key = lambda x:x[2])

print(graph)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0] * (N+1)
for i in range(1, N+1):
    parent[i] = i

map = []
for i in graph:
    a = i[0]
    b = i[1]
    c = i[2]
    if find_parent(parent, a) == find_parent(parent, b):
        pass
    else:
        union_parent(parent, a, b)
        map.append((a, b, c))

map.sort(key = lambda x:x[2])

print(map)

#유지 비용이 가장 큰 경로의 유지비 제외
sum = 0
for i in range(len(map)-1):
    sum += map[i][2]

print(sum)

#자체 평가 : 솔루션과 아이디어가 동일. 최소 신장 트리를 구한 뒤 비용이 가장 큰 경로 하나를 제거하는 방향