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

print('테스트 케이스 개수 T 입력')
T = int(input())

case = []

print('테스트 케이스 정보 입력')
for i in range(T):
    n, m = map(int, input().split())
    info = list(map(int, input().split()))
    case.append(((n, m), info))

print(case)

def max_count(case):
    map = []
    n, m = case[0][0], case[0][1]
    for i in range(n):
        line = []
        for j in range(m):
            line.append(case[1][m*i+j])
        map.append(line)
    
    max = 0
    
    for i in range(n):
        count = map[i][0]
        for j in range(1, m):
            
            
        
    
    return

print(max_count(case[0]))