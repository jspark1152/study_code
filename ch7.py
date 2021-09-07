#이진 탐색
#리스트 내에서 데이터를 매우 빠르게 탐색하는 알고리즘

#순차 탐색(Sequential Search) : 리스트 안의 특정 데이터를 찾기 위해 데이트를 하나씩 차례대로 확인
#보통 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 사용
#데이터가 아무리 많아도 시간만 충분하다면 원하는 데이터를 찾을 수 있다는 장점이 있음

#순차 탐색 코드
def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1

print('생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력')
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print('앞서 적은 원소 개수만큼 문자열을 입력. 구분은 띄어쓰기 한 칸으로 함')

array = input().split()

print(sequential_search(n, target, array))

#이진 탐색(Binary Search) : 반으로 쪼개면서 탐색
#이진 탐색은 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있음
#데이터가 무작위일 때는 사용할 수 없지만 정렬되어 있는 경우 매우 빠르게 데이터를 찾을 수 있음
#탐색 범위를 절반씩 좁혀가며 데이터를 탐색
#위치를 나타내는 변수 3개를 사용 = 시작점, 중간점, 끝점
#찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교
#찾고자 하는 데이터와 중간점 데이터를 비교
#중간점이 더 큰 경우 끝점을 중간점으로 당겨옴
#중간점이 더 작은 경우 시작점을 중간점으로 당겨옴
#이를 반복하여 중간점과 찾고자 하는 데이터의 지점이 일치할 경우 종료

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2

    if target < array[mid]:
        end = mid-1
        return binary_search(array, target, start, end)
    elif target > array[mid]:
        start = mid+1
        return binary_search(array, target, start, end)
    elif target == array[mid]:
        return mid

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

a = binary_search(array, 13, 0, 11)

print(a)

#반복문으로 이진 탐색 구현
def bin_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            end = mid-1
        elif target > array[mid]:
            start = mid+1
    return None

print('원수 개수와 찾을 데이터 입력')
n, target = map(int, input().split())

print('전체 원소 입력')
array = list(map(int, input().split()))

result = bin_search(array, target, 0, n-1)

print(result)

#트리 자료구조
#노드와 노드의 연결로 표현
#노드는 정보의 단위로서 어떠한 정보를 가지고 있는 개체
#그래프 자료구조의 일종으로 DB 시스템이나 파일 시스템과 같은 많은 양의 데이터를 관리하기 위한 목적으로 사용

#특징
#1. 트리는 부모 노드와 자식 노드의 관계로 표현
#2. 트리의 최상단 노드를 루트 노드
#3. 트리의 최하단 노드를 단말 노드
#4. 트리에서 일부를 떼어내도 트리 구조이며 이를 서브 트리라고 함
#5. 트리는 파일 시스템과 같이 계층적이고 정렬된 데이터를 다루기에 적함

#이진 탐색 트리 : 이진 탐색이 동작할 수 있도록 고안된 구조
#모든 트리가 이진 탐색 트리는 아니며 다음 특징을 가짐
#1. 부모 노드보다 왼쪽 자식 노드가 작다
#2. 부모 노드보다 오른쪽 자식 노드가 크다

#과정은 다음과 같음
#루트 부모 노드부터 찾고자 하는 데이터를 비교
#데이터가 부모 노드보다 클 경우 좌측 자식 노드는 버리고 우측 자식 노드로 이동
#데이터가 부모 노드보다 작을 경우 우측 자식 노드는 버리고 좌측 자식 노드로 이동
#이를 데이터를 찾을 때 까지 반복

#이진 탐색 문제는 데이터가 많거나 탐색 범위가 매우 넓은 편
#sys 라이브러리의 readline() 함수를 이용하면 시간 초과를 피할 수 있음

import sys
input_data = sys.stdin.readline().rstrip()
print(input_data)

#한 줄 입력 후 엔터 입력시 줄바꿈으로 입력되기에 rstrip() 함수를 사용해야 함
