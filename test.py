from collections import deque

print('노드 n, 간선 m')
n, m = map(int, input().split())

graph = []
print('간선 정보')
for i in range(m):
    a, b = map(int, input().split())
    graph.append((a, b))

ent = [0] * (n+1)

for i in graph:
    ent[i[1]] += 1

visited = [False] * (n+1)
map = []

def top_sort(graph):
    q=deque()
    for i in range(1, n+1):
        if ent[i] == 0:
            q.append(i)
            visited[i] = True
    
    while q:
        a = q.popleft()
        map.append(a)
        graph = [i for i in graph if i[0] != a]

        link = [0] * (n+1)
        for i in graph:
            link[i[1]] += 1
        
        for i in range(1, n+1):
            if link[i] == 0 and not visited[i]:
                q.append(i)
                visited[i] = True

top_sort(graph)
print(map)

