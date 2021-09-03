#처음부터 다시.. 왜 안되는거여 대체 ㅡㅡ

print('얼음 케이스 사이즈')
n, m = map(int, input().split())

print('케이스 형태 결정')
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x, y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1 #방문처리
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1


print(result)
