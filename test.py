print('얼음틀의 사이즈를 입력')
N, M = map(int, input().split())

case = [[0] * M for _ in range(N)]

for i in range(N):
    case[i] = list(map(int, input().split()))


#0인 값들을 노드 처리를 해야할텐데 어떻게?

from collections import deque

hole_list = []

for i in range(N):
    for j in range(M):
        if case[i][j] == 0:
            hole_list.append([i, j])

print('Hole List = ', hole_list)


mark = []
node = [[] for _ in range(N*M)]
stack = []

def ice_node(stack):
    global n
    global node
    global mark
    global hole_list
    
    while stack:
        
        a = stack[-1]
        
        if a not in node[n]:
            node[n].append(a)
        if a not in mark:
            mark.append(a)
            
        for i in [1, -1]:
            if [a[0]+i, a[1]] in hole_list and [a[0]+i, a[1]] not in mark:
                stack.append([a[0]+i, a[1]])
                ice_node(stack)
            elif [a[0], a[1]+i] in hole_list and [a[0], a[1]+i] not in mark:
                stack.append([a[0], a[1]+i])
                ice_node(stack)
            else:
                pass
        
        stack.pop()
        
        
        
n = 0

for m in range(len(hole_list)):
    a = hole_list[m]
    stack.append(a)
    
    if a not in mark:
        ice_node(stack)
    
    n += 1

node = [i for i in node if len(i) != 0]

print('node : ', node)