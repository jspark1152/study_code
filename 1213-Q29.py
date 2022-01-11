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
array = []
for _ in range(N):
    array.append(int(input()))
    
array.sort()

#아 겁나 생각이 안난다.. 며칠째 고민중.. 조합으로 뽑아내서 다하는건 아닌거 같은데 ㅡㅡ

#모범답안을 봐도 후.. 이해가 안간다 ㅁㅊ거 아닌가..

start = array[1] - array[0] #두 집간의 거리 최소값
end = array[-1] - array[0] #두 집간의 거리 최대값
result = 0

while(start <= end): #이진 탐색
    mid = (start+end) // 2 #이진 탐색을 집 위치 기준이 아니라 거리 최소 최대를 기준으로 잡네
    value = array[0] #이것의 역할은?
    count = 1 #count는 아무래도 설치한 공유기 개수인듯 > 그러면 위에 value는 공유기 설치 위치? 첫 번째 집에 우선 설치
    for i in range(1, N): #0을 건너뛰는 이유는 0위치에 이미 공유기를 설치했기 때문
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)