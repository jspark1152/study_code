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