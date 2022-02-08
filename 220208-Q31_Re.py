print('맵 정보 입력')
n, m = map(int, input().split())

info = list(map(int, input().split()))
print(n, m, info)

map = []
for i in range(m):
    array = []
    for j in range(n):
        array.append(info[j*m + i])
    map.append(array)

print(map)

for i in range(1, m):
    for j in range(n):
        #좌상단에서 접근
        if j == 0:
            left_u = 0
        else:
            left_u = map[i-1][j-1]
        
        #좌측에서 접근
        left = map[i-1][j]
        
        #좌하단에서 접근
        if j == n-1:
            left_d = 0
        else:
            left_d = map[i-1][j+1]
        
        #최대값으로 갱신
        map[i][j] = map[i][j] + max(left_u, left, left_d)

print(map)

result = 0
for i in range(n):
    result = max(result, map[m-1][i])
    
print(result)

#자체 평가 : map 을 열 벡터로 구현해봤음. 역시 아이디어가 중요함. 코딩 게을리하지 않도록 하자