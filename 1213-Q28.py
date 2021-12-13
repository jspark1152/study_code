'''
고정점 찾기

고정점 : 수열 원소 중 그 값이 인덱스와 동일한 원소를 의미
하나의 수열이 N개의 서로 다른 원소를 포함하고 있으며, 모든 원소가 오름 차순으로 정렬
이 수열에 고정점이 있다면 고정점을 출력하는 프로그램을 작성
고정점은 최대 1개만 존재
없다면 -1 출력

입력 조건
1. 첫 줄에 N 입력
2. 다음 줄에 N개의 원소가 공백으로 구분되어 입력

출력 조건 : 고정점을 출력. 단, 고정점이 없다면 -1 출력
'''

print('N 입력')
N = int(input())

print('수열 정보 입력')
lst = list(map(int, input().split()))

#이진 탐색 이용? How?

def find_fixedpt(lst, start, end):
    while start <= end:
        mid = (start+end)//2
        if lst[mid] == mid:
            return mid
        elif lst[mid] < mid: #left 사이드는 볼 필요가 없음. 원소는 서로 모두 다르기 때문.
            start = mid+1
        elif lst[mid] > mid:
            end = mid-1         
    return None

result = find_fixedpt(lst, 0, N-1)

if result == None:
    print(-1)
else:
    print(result)
    
#자체 평가 : 문제에 주어진 조건이 매우 강한 편이어서 구현이 쉬웠음