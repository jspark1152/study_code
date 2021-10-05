graph = []
for i in range(5):
    a, b = map(int, input().split())
    graph.append((a, b))

print(graph)

graph.sort(key = lambda x:x[1])

print(graph)