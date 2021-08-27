#문제를 풀면서 자신만의 라이브러리를 만들어 관리
#알고리즘 학습 후 소스코드를 보기 좋게 정리하는 습관 가지기

#2차원 리스트 회전 알고리즘 구현 - 직접 완
def rotate_90_list(a):
    #a는 row_len, col_len 사이즈
    row_len=len(a)
    col_len=len(a[0])

    #rot(a를 90도로 회전)은 col_len, row_len 사이즈로
    rot = [[0]*row_len for _ in range(col_len)]

    #원리는 행렬의 rotate 개념을 응용
    for i in range(row_len):
        for j in range(col_len):
            rot[col_len-1-j][i] = a[i][j]
    
    return(rot)

b=[[0,1,2],[3,4,5]]

print(rotate_90_list(rotate_90_list(rotate_90_list(rotate_90_list(b)))))

#소수 판별
#이런 경우 시간 복잡도=O(x)로 비효율적
def prime_no(x):
    if x == 2:
        return True
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

#따라서 약수의 대칭성을 이용 > 제곱근까지만 확인
import math

def prime_no(x):
    if x == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                return False
        return True
print(prime_no(2))
print(prime_no(131))

#에라토스테네스의 체 : 여러 개의 수가 소수인지를 판별
#2부터 시작하여 2를 제외한 2의 배수를 그 배열에서 모두 제거
#2 보다 큰 다음수가 배열에 존재할 경우 그 수를 제외한 그 수의 배수를 그 배열에서 모두 제거
#이를 반복 
def eratostenes(n):
    list = [i+2 for i in range(n-1)]

    a = list[0] #이 값은 2임
    
    for k in range(n):
        if a+k in list:
            for i in range(2,n):
                list = [p for p in list if p != (a+k)*i]
        else:
            pass
    return list

print(eratostenes(10))

#아래 방식이 훨씬 빠름
import math
n=1000
array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True:
        j = 2
        while i*j <= n:
            array[i*j] = False
            j+=1

print(array)

for i in range(2, n+1):
    if array[i]:
        print(i, '\t', end='')

#수정 가능?
def eratostenes(n):
    list = [i+2 for i in range(n-1)]

    a = list[0] #이 값은 2임
    
    #여기서 핵심은 입력된 n 값의 제곱근까지만 확인한다는 것(약수의 성질)
    for p in range(2, int(math.sqrt(n))+1):
        q = 2
        while p*q <= n:
            list = [i for i in list if i != p*q]
            q+=1
    return list

print(eratostenes(1000))

#투 포인터

#주어진 list의 연속된 특정 부분합을 가지는 부분 list 출력
a = [1, -2, 9, 3, 2, 5, 4]

def list_partial_sum(n):
    count = 0
    for i in range(len(a)):
        sum = 0
        for j in range(len(a)-i):   
            sum += a[i+j]
            if sum == n:
                count += 1
                print(a[i:i+j+1])
    return count
        
print(list_partial_sum(7))

#이를 투포인터 형식으로 수정
#시작과 끝 포인터를 지정
#끝 포인터를 먼저 미루고 다음 시작점을 당기는 것을 반복
#단 음수가 포함되는 경우 문제가 발생
a = [1, 2, 3, 2, 5]

def list_partial_sum(n):
    sum = 0
    end = 0
    count = 0
    for i in range(len(a)):     
        while sum < n and end< len(a):
            sum += a[end]
            end += 1

        if sum == n:
            count += 1
            print(a[i: end])
        sum -= a[i]
    print(count)

print(list_partial_sum(5))

#주어진 두 리스트의 합집합

a=[1,2,3]
b=[4,5]

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
                i += 1
            else:
                c[k] = b[j]
                j += 1
        elif i == n and j < m:
            c[k] = b[j]
            j += 1
        elif j == m and i < n:
            c[k] = a[i] 
            i += 1
        else:
            pass
    return c

print(list_union(a,b))  
    
#접두사 합
data=[10, 20, 30, 40, 50]

sum=0
prefix_sum=[]
for i in data:
    sum += i
    prefix_sum.append(sum)

print(prefix_sum)

#구간 합
def par_sum(l,r):
    return prefix_sum[r-1]-prefix_sum[l-2]

print(par_sum(2,3))
