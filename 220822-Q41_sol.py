'''
음.. 원래는 서로소 집합 알고리즘 이용해서 모든 여행지(노드)가 한 그룹에 속해있는지 그 여부를 따지면 됨
'''

#서로소 알고리즘 까먹고 있었음.
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
        
n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i
    
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1: #i 에서 j 가 연결되어 있다는 의미
            union_parent(parent, i+1, j+1) #연결되어 있으니 union

plan = list(map(int, input().split()))

result = True

for i in range(m-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]): #여행 계획에 포함된 여행지가 서로 연결되어 있지 않을 때
        result = False

if result == True:
    print('YES')
else:
    print('NO')