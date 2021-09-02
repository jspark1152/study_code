#BFS = Breath First Search : 너비 우선 탐색
#가까운 노드부터 탐색
#DFS는 최대한 멀리 있는 노드를 우선으로 탐색하는 방식이지만 BFS는 그 반대
#BFS 구현은 선입선출 방식인 Queue 자료 구조를 이용
#인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 작성

#동작 방식은 다음과 같음
#1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
#2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
#3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복



from collections import deque

def bfs_ft(graph, v, visited):   
    queue = deque()
    queue.append(v)

    visited[v] = True

    while queue: #큐가 공집합이 될때까지 반복한다는 의미, 기억해두자
        a = queue.popleft()
        print(a, end = '')
        for j in graph[a]:
            if not visited[j]:
                visited[j] = True
                queue.append(j)
            else:
                pass

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
bfs_ft(graph, 1, visited)
