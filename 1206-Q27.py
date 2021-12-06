'''
정렬된 배열에서 특정 수의 개수 구하기

N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬
이 수열에서 x 가 등장하는 횟수 출력

입력조건
1. 첫줄에 N과 x가 정수 형태로 공백으로 구분되어 입력
2. 다음 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력

출력조건 : 수열의 원소 중에서 값이 x인 원소의 개수를 출력. 단, 하나도 없다면 -1 을 출력
'''

print('N과 x를 입력')
N, x = map(int, input().split())

print('수열 입력')
array0 = list(map(int, input().split()))

result = 0
for i in range(len(array0)):
    if array0[i] == x:
        result += 1

if result == 0:
    print(-1)
else:
    print(result)