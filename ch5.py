#탐색 : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
#탐색 알고리즘으로 DFS 와 BFS 
#자료구조 : 데이터를 표현하고 관리하고 처리하기 위한 구조
#스택과 큐는 자료구조의 기초
#Push(데이터 삽입) / Pop(데이터 삭제) 두 핵심 함수로 구성
#오버플로 : 특정 자료구조가 수용할 수 있는 데이터의 크기를 이미 가득 찬 상태에서 삽입 수행할 때 발생
#언더플로 : 특정 자료구조에 데이터가 없는 상태에서 삭제 연산을 수행할 때 발생

#Stack
#박스 쌓기에 비유 : 박스는 아래에서부터 위로 쌓음
#아래 박스를 치우기 위해선 그 위에 올려둔 박스를 치워야함
#이를 선입후출 = First in Last out 또는 후입선출 = Last in First out

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1]) #최상단 원소부터 출력

#파이썬에서는 스택 이용할 때 별도 라이브러리 사용이 필요없음
#기본 리스트에 append()/pop() 메서드를 이용하면 스택과 동일하게 동작

#Queue
#대기 줄에 비유 : 흔히 놀이공원에 입장하기 위해 줄을 설 때, 먼저 온 사람이 먼저 들어가게 됨
#이를 선입선출 = First in First out

from collections import deque

#Queue 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

#재귀 함수 : 자기 자신을 호출하는 함수

def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

#recursive_function() 실행 시 무한히 반복됨

#재귀 함수의 종료 조건
#언제 끝날지 명시를 해야함

def recursive_function(i):
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀 함수를 종료합니다.')

recursive_function(1)

#팩토리얼 예제
#반복으로 구현한 n!
def fac_iter(n):
    result = 1
    for i in range(i, n+1):
        result *= i
    return result

#재귀적으로 구현한 n!
def fac_recur(n):
    if n <= 1:
        return 1
    
    return n * fac_recur(n-1) #n! = n * (n-1)! 이용

print('반복적으로 구현 : ', fac_iter(10))
print('재귀적으로 구현 : ', fac_recur(10))

#재귀 함수를 사용하면 좀더 간결
#단, 재귀 함수 사용할 때는 역시나 종료 조건 반드시 넣어줘야함