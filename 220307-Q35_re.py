N = int(input())

list_ugly = [1]

for i in range(N):
    
    a = 2*list_ugly[i]
    b = 3*list_ugly[i]
    c = 5*list_ugly[i]
    if a not in list_ugly:
        list_ugly.append(a)
        
    if b not in list_ugly:
        list_ugly.append(b)
        
    if c not in list_ugly:
        list_ugly.append(c)

    list_ugly.sort()

print(list_ugly)

print(list_ugly[N-1])

#자체 평가 : 1000 입력시 결과 출력이 확실히 빠름
#아이디어는 1부터 2, 3, 5를 곱하고 이를 포함시키는 과정