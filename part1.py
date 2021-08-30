#복잡도 계산
#시간 복잡도 : 연산이 몇번 수행되는지를 나타냄
#공간 복잡도 : 메모리를 얼마나 사용하는지를 나타냄

#선택 정렬과 기본 정렬 라이브러리의 수행 시간 비교

from random import randint
import time

array = []
for _ in range(10000):
    array.append(randint(1,100)) #1부터 100 사이의 랜덤 정수를 삽입

#선택 정렬 프로그램 성능 측정
start_time = time.time()

#선택 정렬 프로그램 소스코드
for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

end_time = time.time() #측정 종료
print('선택 정렬 성능 측정 : ', end_time-start_time) #수행시간 출력


#배열을 다시 초기화
array = []
for _ in range(10000):
    array.append(randint(1,100))

#기본 정렬 라이브러리 성능 측정
start_time = time.time()

array.sort()

end_time = time.time()
print('기본 정렬 라이브러리 성능 측정 : ', end_time-start_time)

#코딩 테스트는 프로그래밍 실력이 아닌 문제 해결 능력을 평가
#기초 알고리즘에 기반한 문제 출제
#출제 빈도가 높은 문제는 그리디, 구현, DFS/BFS를 활용한 탐색 문제
