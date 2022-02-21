'''
오늘부터 N+1일째 되는 날 퇴사하기 위해 남은 N일 동안 최대한 많은 상담을 진행
하루에 하나씩 서로 다른 사람의 상담을 잡음
각각 상담을 완료하는데 걸리는 기간 T_i, 상담 금액 P_i

상담을 적절히 했을 때 얻을 최대 수익을 구하는 프로그램 작성

입력조건
1. 첫 줄에 N(1이상 15이하) 입력
2. 다음 줄부터 N개의 줄에 T, P가 공백으로 구분 되어 주어짐

출력 조건 : 첫줄에 얻을 수 있는 최대 이익 출력
'''

print('N 입력')
N = int(input())

print('상담 정보 입력')
info = []
for i in range(N):
    a, b = map(int, input().split())
    info.append((a, b))

print(info)

dp = [0] * (N+1)
max_val = 0

for i in range(N-1, -1, -1): #끝날부터 거슬러서 확인
    time = info[i][0] + i
    
    #상담이 기간안에 끝나는 경우
    if time <= N:
        #상담이 끝난 뒤 해당 상담비용과 그 다음날부터의 수익 고려
        dp[i] = max(info[i][1] + dp[time], max_val)
        max_val = dp[i]
        
    #상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_val
        
    print(dp)

print(max_val)

#자체 평가 : 생각보다 어렵다. 주기적으로 복습이 필요한 문제로 보임. 아이디어가 멋있다.