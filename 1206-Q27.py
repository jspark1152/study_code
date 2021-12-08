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

#이진 탐색으로 구현
def find_first(list, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if list[mid] == target:
            if list[mid-1] != target:
                return mid
            else:
                end = mid-1
        elif list[mid] > target:
            end = mid-1
        elif list[mid] < target:
            if list[mid+1] == target:
                return mid+1
            else:
                start = mid+1
    return None

def find_last(list, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if list[mid] == target:
            if list[mid+1] != target:
                return mid
            else:
                start = mid+1
        elif list[mid] > target:
            start = mid+1
        elif list[mid] < target:
            if list[mid-1] == target:
                return mid-1
            else:
                end = mid-1
    return None

s = find_first(array0, x, 0, N-1)
e = find_last(array0, x, 0, N-1)
print(s, e)

#오류 : mid+1 or mid-1 의 list 값 호출에서 오류 발생;; 

'''
result = 0
for i in range(len(array0)):
    if array0[i] == x:
        result += 1

if result == 0:
    print(-1)
else:
    print(result)
'''

#자체 평가 : 의도가 이게 아닌듯 함. for 문 자체 시간복잡도가 O(N) 으로 알고 있...
#이진 탐색으로 구현해야하나?\

