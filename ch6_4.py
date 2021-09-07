#실전 문제 : 두 배열의 원소 교체
#두 개의 배열 A와 B는 N개의 자연수 원소로 구성
#최대 K번의 바꿔치기 연산을 수행
#최종 목표는 A의 모든 원소 합이 최대가 되도록

#첫 줄에 N, K가 공백으로 구분되어 입력(1<= N <= 100,000   0<=K<=N)
#다음 줄에 배열 A의 원소들이 공백으로 구분되어 입력(10,000,000 미만의 자연수)
#세번째 줄에 배열 B의 원소들이 공백으로 구분되어 입력(10,000,000 미만의 자연수)

#출력 조건 : 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소 합의 최댓값 출력

print('N과 K 입력')
N, K = map(int, input().split())

print('배열 A 입력')
A = list(map(int, input().split()))

print(A)

print('배열 B 입력')
B = list(map(int, input().split()))

print(B)

#1. A와 B 오름차순 정렬부터 수행
#2. A의 인덱스가 가장 작은것 <> B의 인덱스가 가장 큰것
#3. 그 다음 안쪽 인덱스끼리 교환 
#원소를 서로 교환할 것인가 아니면 비교하여 큰 것을 택하여 더할 것인가
#후자로 해보자

A = sorted(A)
B = sorted(B)

print(A)
print(B)

A_sum = 0

for i in range(K):
    if A[i] <= B[N-i-1]:
        A_sum += B[N-i-1]

for j in range(K, N):
    A_sum += A[j]

print(A_sum)

#자체 평가 : 쉬움. 


