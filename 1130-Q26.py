'''
카드 정렬하기
정렬된 두 묶음의 숫자 카드가 있을 때 각 묶음의 카드 수를 A, B
이를 합쳐서 비교를 하려면 A + B 번의 비교를 수행해야 함
책상 위에 매우 많은 카드 묶음이 놓여있을 때 비교 수행이 가장 최소가 되도록 하는 프로그램을 작성

입력 조건
1. 첫 줄에 카드 묶음 수 N 이 주어짐
2. 다음 줄부터 N 개의 줄에 걸쳐 카드 묶음의 크기가 주어짐

출력 조건 : 첫 줄에 최소 비교 횟수를 출력
'''

print('카드 묶음 수 입력')
N = int(input())

from queue import deque
print('각 카드 묶음의 카드 장수 입력')
card = []
for i in range(N):
    card.append(int(input()))

#크기 순대로 정렬
card.sort()
card = deque(card)
print(len(card))

#장수가 가장 작은 두 묶음을 비교해나가는 것이 포인트
sum = 0
while len(card) != 1:
    a = card.popleft()
    b = card.popleft()
    sum = sum + a + b
    #두 묶음을 하나의 묶음으로
    card.append(a + b)
    #추가된 새로운 하나의 묶음에 대한 정렬이 필요
    card = list(card)
    card.sort()
    card = deque(card)

print(sum)

#자체 평가 : 크게 어렵진 않았음. 그런데 deque을 구현하는데 있어서 정렬을 바로 쓸 수는 없나?