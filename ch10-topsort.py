from collections import deque

print('노드 N, 간선 M')
N, M = map(int, input().split())

graph = []

print('간선 정보 입력 a 에서 b')
for i in range(M):
    a, b = map(int, input().split())
    graph.append((a, b))

print(graph)

#진입 차수 계산
def deg_zero(graph):
    deg = [0] * (N+1)
    for i in graph:
        deg[i[1]] += 1
    return deg

deg = deg_zero(graph)
print(deg)

map = []
q = deque()

def input_q(deg, q):
    for i in range(1, N+1):
        if deg[i] == 0 and i not in map and i not in q:
            q.append(i)
    return

input_q(deg, q)

while q:
    n = q.popleft()
    map.append(n)

    #graph에서 n으로 부터 향하는 방향 성분 제거
    remove_set = []
    for i in graph:
        if i[0] == n:
            remove_set.append(i)
    graph = [i for i in graph if i not in remove_set]
    print(graph)

    #진입 차수 확인
    deg = deg_zero(graph)
    print(deg)
    
    #q에 다시 성분 삽입
    input_q(deg, q)
    print(q)

print(map)

#자체 평가 : 스텝마다 print로 확인하면서 오류 수정해가며 작성. 알고리즘대로 나름 잘 짠듯 함.