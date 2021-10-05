#노드 N, 간선 M 입력
print('노드 N, 간선 M')
N, M = map(int, input().split())

parent = [0] * (N+1)

for i in range(1, N+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

graph = []
#간선 정보 입력
print('간선 정보 a 에서 b 까지의 비용 c')
for _ in range(M):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

#비용 오름차순으로 정렬
graph.sort(key = lambda x:x[2])

map = []

#Cycle 구분
for i in range(M):
    a = graph[i][0]
    b = graph[i][1]

    if find_parent(parent, a) == find_parent(parent, b):
        pass #Cycle을 발생시키는 구간
    else:
        union(parent, a, b)
        map.append((a, b))

print(map)

#자체 평가 : list에서 특정 성분 정렬법을 몰라서 찾아봄. Cycle 구분법 구현해봄. 서로소 구분하는 find와 union 구현에는 문제가 없어보임.
