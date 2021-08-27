a=[1,2,3]
b=[2,4,5]

def list_union(a,b):
    a.sort()
    b.sort()

    n = len(a)
    m = len(b)

    c = [0] * (n+m) #합리스트 초기화

    i=0
    j=0
    
    for k in range(n+m):
        if i < n and j < m:
            if a[i]<=b[j]:
                c[k] = a[i]
                i+=1 # i+1 이라고 해서 삽질했음 ㅡㅡ... 집중.
            else:
                c[k] = b[j]
                j+=1
        elif i == n and j < m:
            c[k] = b[j]
            j+=1
        elif j == m and i < n:
            c[k] = a[i] 
            i+=1
        else:
            pass
    return c

print(list_union(a,b))