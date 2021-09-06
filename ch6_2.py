#실전 문제 : 위에서 아래로

#하나의 수열에는 다양한 수 존재
#수는 크기에 상관없이 나열
#이 수를 큰수부터 작은 수의 순서로 정렬
#수열을 내림차순으로 정렬

#첫 줄에 수열에 속한 수의 개수 N(1이상 500이하)이 선언
#둘째줄부터 N+1번째 줄까지 N개의 수가 입력(수의 범위 : 1이상 100,000이하 자연수)

#출력 조건 : 입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분하여 출력
#동일한 수의 순서는 자유롭게 출력

print('수열에 포함될 수 개수 N 선언')
N = int(input())

array = []

print('수열에 포함될 수 N개 입력')

for i in range(N):
    array.append(int(input()))

print(array)

array = sorted(array, reverse=True)

print(array)

for i in array:
    print(i, end=' ')