#정렬 Sorting : 데이터를 특정한 기준에 따라서 순서대로 나열
#정렬 알고리즘으로 데이터를 정렬하면 이진 탐색(Binary Search)이 가능
#선택 정렬 / 삽입 정렬 / 퀵 정렬 / 계수 정렬

#선택 정렬
#데이터가 무작위로 여러 개 있을 때, 이 중 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고 그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i

    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    
    array[i], array[min_index] = array[min_index], array[i]

print(array)

#시간복잡도 O(N^2)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

array.sort() #기본 정렬라이브러리 사용하는것이 훨씬 빠름

print(array)

#삽입 정렬
#구현 난이도가 선택 정렬보다 높은 편이지만 실행 시간 측면에서 효율적
#특정 데이터를 적절한 위치에 삽입

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)

#포인트는 거의 정렬되어 있는 상태에서는 삽입 정렬이 효과적

#퀵 정렬
#정렬 알고리즘 중 가장 많이 사용
#피벗 : 데이트들을 교환하기 위한 '기준'
#퀵 정렬 수행 전 피벗을 어떻게 설정할지 명시
#피벗을 설정하고 리스트를 분할하는 방법에 따라 구분됨
#호어 분할 방식이 대표적
#호어 분할 방식에서는 다음 규칙에 따라 피벗을 설정
#1. 리스트에서 첫 번째 데이터를 피벗으로 정함
#2. 피벗을 제외한 좌측에서부터 피벗보다 큰 값을 찾고 우측에서부터는 피벗보다 작은 값을 찾음
#3. 찾은 뒤에 이 두 값을 서로 교환
#4. 다시 2번으로 돌아가서 반복
#5. 반복 중 좌측에서부터 찾아가던 위치와 우측에서부터 찾아가던 위치가 서로 교차할 때 작은 데이터를 피벗과 교환
#6. 그러면 피벗을 기준으로 좌측에는 피벗보다 작은 값 우측에는 피벗보다 큰 값들로 구성
#7. 이를 분할된 상태라고 하며 다시 좌측과 우측에 대하여 1번으로 돌아가서 반복

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end
    while left <= right:
        #왼쪽에서 부터 피벗보다 큰 수를 찾을 때 까지 left 인덱스를 1씩 증가
        while left <= end and array[left] <= array[pivot]:
            left += 1
        
        #오른쪽에서 부터 피벗보다 작은 수를 찾을 때 까지 right 인덱스를 1씩 감소
        while right > start and array[right] >= array[pivot]:
            right -= 1
        
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    #반복문이 시행되고 나면 피벗을 기준으로 피벗보다 작은 값들은 왼쪽, 큰 값들은 오른쪽에 위치
    #이를 분할된 상태라고 함

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)

#파이썬에서의 퀵 정렬 
#기억해두자 매우 심플함
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x < pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

#계수 정렬
#특정 조건이 부합할 때 사용할 수 있지만 매우 빠름
#별도의 리스트를 선언하고 그 안에 정렬에 대한 정보를 담음

#0 ~ 9 까지 정렬하는 경우 길이가 10인 리스트를 선언하고 그 인덱스에 누적된 데이터 값을 기반으로 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

list = [0] * (max(array)+1)

for i in range(len(array)):
    list[array[i]] += 1

result = []
for i in range(10):
    for _ in range(list[i]):
        result.append(i)

print(result)


