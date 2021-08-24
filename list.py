#리스트는 여러 개의 데이터를 연속적으로 담아 처리
#배열 Array 기능을 포함
#append(), remove() 등을 지원

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

print(a[0])

a = list() #Empty list 선언
print(a)
a = []
print(a)

#크기가 n인 1차원 리스트 초기화 방법
n = 10
a = [0] * n
print(a)

a[0] = 1
print(a)

#리스트 Indexing / Slicing
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a)

print(a[-1]) #뒤에서 첫번째 원소 출력
print(a[-3]) #뒤에서 세번째 원소 출력

a[3] = 7 #리스트의 네번째 원소 값 변경
print(a)

print(a[0:3]) #a 리스트의 첫 성분부터 4번째 전 성분까지 Slice

#리스트 컴프리헨션은 리스트를 초기화하는 방법 중 하나
#대괄호 안에 조건문/반복문을 넣는 방식으로 초기화

array = [i for i in range(20) if i%2==1]
print(array)

#위 방식의 원래 정석 표현은 다음과 같음
array=[]
for i in range(20):
    if i%2==1:
        array.append(i)
print(array)

array = [i*i for i in range(1,10)]
print(array)

#2차원 리스트를 초기화할 때 효과적으로 이용 가능
n=3
m=4
array = [[0]*m for _ in range(n)] # _ 는 반복 수행시 변수를 무시하고자 할 때 사용
print(array)

array[1][2]=5
print(array)

#2차원 리스트를 다음과 같이 초기화한다면 문제가 발생
array = [[0]*m]*n
print(array)
array[1][2]=5
print(array) #결과가 이전 결과와 다른 것을 확인할 수 있음
#[[0]*m] 의 리스트를 내부적으로 동일한 n개의 객체로 인식하게 됨
#따라서 반드시 2차원 리스트 초기화시에는 리스트 컴프리헨션을 이용!

#리스트 관련 메서드
#append()/sort()/reverse()/insert()/count()/remove()
a = [1, 4, 3]
print('기본 리스트 : ', a)

a.append(2)
print('삽입 : ', a)

a.sort()
print('오름차순 정렬 : ', a)

a.sort(reverse = True)
print('내림차순 정렬 : ', a)

a.reverse()
print('원소 뒤집기 : ', a)

a.insert(2, 4)
print('인덱스2에 4 추가 : ', a)

print('값이 4인 데이터 수 : ', a.count(4))

a.remove(4)
print('값이 4인 데이터 하나 삭제 : ', a)

#주의할 사항
#append()는 리스트의 원소 개수가 N개 일 때 시간 복잡도가 O(1)
#insert()는 리스트의 원소 개수가 N개 일 때 시간 복잡도가 O(N) : 원소를 삽입한 뒤 나머지 원소들의 위치 조정 필요
#따라서 insert()를 남발하면 굉장히 느려짐

#특정 값이 한개 이상일 때 모두 제거하는 방법
a = [1, 2, 3, 4, 5, 5, 5]

a = [i for i in a if i != 5]
print(a)

#또는 제거할 성분의 Set을 이용
a = [1, 2, 3, 4, 5, 5, 5]
remove_set={3, 5}

a = [i for i in a if i not in remove_set]
print(a)