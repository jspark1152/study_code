#자주 사용되는 주요 라이브러리의 문법과 유의할 점
#표준 라이브러리 : 자주 사용되는 표준 소스코드를 미리 구현해놓은 라이브러리

#내장 함수 : print(), input(), sorted() 등
#itertools : 박복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리
#heapq : 힙 기능을 제공하는 라이브러리로 우선순위 큐를 구현하기 위해 사용
#bisect : 이진 탐색 기능을 제공하는 라이브러리
#collections : deque, Counter 등의 유용한 자료구조를 포함하고 있는 라이브러리
#math : 필수적인 수학적 기능을 제공하는 라이브러리

#내장 함수 : import 없이 바로 사용 가능
a=[i for i in range(1,6)]
print(a)
result = sum(a)
print(result)

result = min(a)
print(result)

result = max(a)
print(result)

#eval() 함수는 수식을 문자열로 입력해줘야 함
result = eval('(3+5)*7')
print(result)

result = sorted([9,1,8,5,4]) #오름차순
print(result)
result = sorted([9,1,8,5,4], reverse=True) #내림차순
print(result)

#x[n]=n+1 번째 값으로 정렬
result = sorted([('홍길동', 35, 1), ('이순신', 75, 2), ('아무개', 50, 3)], key = lambda x: x[1], reverse=True)
print(result)

#-------------------------------------------------------
#itertools : 반복되는 데이터를 처리하는 기능을 포함
#permutations, combinations가 유용하게 사용됨

from itertools import permutations

data = ['A', 'B', 'C']
#data에서 3개를 선택하여 모든 순열 구하기
result = list(permutations(data, 3))
print(result)

from itertools import combinations

result = list(combinations(data, 2))
print(result)

from itertools import product

#product : 중복 순열을 계산. 단, product는 class이므로 list 자료형으로 변환

#result = product(data, repeat=2)
result = list(product(data, repeat=2))
print(result)

#조합을 계산할 때 중복을 허용하는 경우
from itertools import combinations_with_replacement

result = list(combinations_with_replacement(data, 2))
print(result)

#-------------------------------------------------------
#heapq : 힙 Heap 기능을 제공, 우선순위 큐 기능을 구현하고자 할 때 사용

import heapq

def heapsort(iterable):
    h = []
    result = []
    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
        print(h) #파이썬에서 힙은 자동으로 오름차순 정렬이 완료
    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
        print(result)
    return result

test = heapsort([3,1,5,7,9,2,4,6,8,0])

print(test)

#내림차순 구현은 다음과 같이 - 부호를 이용
def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
        print(h)
    for i in range(len(h)):
        result.append(heapq.heappop(h)*-1)
        print(result)
    return result

test = heapsort([1,3,5,7,9,2,4,6,8,0])

print(test)

#-------------------------------------------------
#bisect : 이진 탐색을 쉽게 구현
#정렬된 배열에서 특정 원소를 찾아야 할 때 효과적
#bisect_left(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾음
#bisect_right(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾음

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

#정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수를 구할 때 효과적

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_by_range(a, 4, 4))

print(count_by_range(a, -1, 3))

#------------------------------------------------------
#collections : 유용한 자료구조를 제공
#deque을 사용해 큐를 구현

from collections import deque

data = deque([2, 3, 4])
data.append(5) #마지막 인덱스 데이터에 이어서 삽입
print(data)
data.appendleft(1) #첫번째 인덱스 데이터 앞에 삽입
print(data)
print(list(data))
data.pop() #마지막 인덱스 데이터 제거
print(data)
data.popleft() #첫번째 인덱스 데이터 제거
print(data)

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue']) #'blue' 등장 횟수
print(counter['green']) #'green' 등장 횟수
print(dict(counter)) #사전 자료형으로 변환 색상이 key, 횟수가 value로 변환된 것을 확인 가능

a = dict()
a['red']=2
a['blue']=3
a['green']=1

print(a)

key_list=a.keys()
value_list=a.values()

for i in key_list:
    print(i, a[i]) #한 번해 봤다. 복습 겸 dic 구현.