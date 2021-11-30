'''
안테나
일직선상의 마을에 여러 채의 집이 위치
이 중 특정 위치의 집에 특별히 한 개의 안테나를 설치
효율성을 위해 모든 집까지의 거리의 총합이 최소가 되도록 설치
안테나는 집이 위치한 곳에만 설치가 가능하며 동일한 위치에 여러개의 집이 존재할 수 있음
집들의 위치 값이 주어질 때 안테나 설치 위치를 선택

입력조건
1. 첫줄에 집의 수 N이 주어짐
2. 다음 줄에 N 채의 집 위치가 공백으로 구분되어 입력

출력조건 : 첫 줄에 안테나를 설치할 위치 값을 출력. 단, 여러 값이 도출될 경우 가장 작은 값 출력
'''

print('집의 개수 입력')
N = int(input())

print('집 위치 입력')
loca = list(map(int, input().split()))

#위치 정렬
loca.sort()

def dist_total(a):
    sum = 0
    for i in range(N):
        sum += abs(a - loca[i])
    
    return sum

#안테나 위치를 어떻게? 집 위치에 다 설치해보는걸로
total = []
for i in range(N):
    sum = dist_total(loca[i])
    print(sum)
    total.append(sum)
print(total)

#거리 합이 가장 작은 곳에 pin을 고정
pin = 0
for i in range(1, N):
    if total[pin] > total[i]:
        pin = i
    print(pin)

print(loca[pin])

#자체 평가 : 조금 더 간결하게 짤 수 없을까..? 고민을 좀 해봐야할 듯