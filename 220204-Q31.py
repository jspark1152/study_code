'''
n X m 크기의 금광
각 칸에 특정 크기의 금이 존재
채굴자는 첫번째 열부터 출발하여 금을 채굴
첫번째 열의 어느 행에서든 출발 가능
이후 오른쪽/오른쪽 위/오른쪽 아래 로만 이동 가능
결과적으로 채굴자가 최대로 채굴할 금의 크기

입력 조건
1. 첫 줄에 테스트 케이스 T 입력
2. 매 테스트 케이스 첫 줄에 n, m이 공백으로 구분되어 입력
3. 그 다음 줄에 매장된 금의 개수 정보 입력(일렬로 입력)

출력 조건 : 테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기 출력
'''

#접근 자체를 잘못한듯 하다
#하.. 역시 머리가 굳은게 분명하다

print('테스트 케이스 수 입력 :')
for tc in range(int(input())):
    print('금광 정보 입력')
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m]) #2차원 테이블 초기화
        index += m
    
    for j in range(1, m):
        for i in range(n):
            #왼쪽 위에서 dp[i][j]로 접근하는 경우
            if i == 0: #왼쪽 위에서 오는 경우가 없음
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            
            #왼쪽 아래에서 dp[i][j]로 접근하는 경우
            if i == n-1: #
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            
            #왼쪽에서 바로 dp[i][j]로 접근하는 경우
            left = dp[i][j-1]
            
            #dp[i][j]의 값을 그 지점에서의 최대값으로 초기화
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    
    print(result)