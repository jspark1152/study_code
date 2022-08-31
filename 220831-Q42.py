'''
공항에는 G개의 탑승구(1~G 번)
공항에는 P개의 비행기가 차례대로 도착할 예정
i 번째 비행기는 gi번째 탑승구 중 하나에 영구적으로 도킹
단, 하나의 탑승구에 한 비행기만 도킹 가능
만약 도킹이 불가능한 경우 공항 운행 중지

입력 조건
1. 첫줄에 탑승구 수 G(1이상 100,000이하) 입력
2. 다음 줄에 비행기 수 P(1이상 100,000이하) 입력
3. 다음 P개의 줄에는 각 비행기가 도킹할 수 있는 탑승구의 정보 gi 입력

출력 조건 : 첫 줄에 도킹 가능한 비행기의 최대 수 출력
'''

print('탑승구 수 G 입력')
G = int(input())
gate = [0 for _ in range(G)]

print('비행기 수 P 입력')
P = int(input())

print('도킹 정보 입력')
info = []
for i in range(P):
    info.append(int(input()))

#해당 비행기 도킹 시 가장 넘버가 큰 게이트에 도킹
def dock(n):
    a = info[n]
    while a-1 >= 0:
        if gate[a-1] == 0:
            gate[a-1] = n+1
            break
        else:
            a -= 1
    if a-1 < 0:
        return 1 #도킹 실패 > 공항 운행 정지
    else:
        return 0

result = 0
for i in range(P):
    stop = dock(i)
    if stop == 0:
        result += 1
    else:
        break
    
print(gate)
print(result)

#자체 평가 : 도킹 구현까진 좋았는데 공항 운행 정지 조건을 주는데 조금 애먹었음. 함수는 또 오랜만에 정의해보는데 다시 자주 써봐야겠음.
#모범 답안에서는 서로소 개념을 이용