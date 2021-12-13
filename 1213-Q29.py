'''
공유기 설치

집 N개가 수직선 위에 존재
각각 집 좌표는 x_1, x_2 ... x_N 이는 모두 다름
집에 인터넷 공유기 C개를 설치하려고 함
한 집에 하나의 공유기만 설치 가능
가장 인접한 두 공유기 사이의 거리를 가능한 크게 설치

입력 조건
1. 첫 줄에 집 개수 N, 공유기 개수 C 입력
2. 다음 줄부터 N개의 줄에 걸쳐 집 좌표 입력

출력 조건 : 가장 인접한 두 공유기 사이의 최대 거리를 출력
'''

#이거 좀 어렵네;;

print('집 개수 N, 공유기 개수 C 입력')
N, C = map(int, input().split())

print('집 위치 정보 입력')
house = []
for _ in range(N):
    house.append(int(input()))
    
house.sort()
print(house)