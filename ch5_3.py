#실전 문제 3. 음료수 얼려 먹기
#N X M 얼음 틀이 있음
#구멍이 난 곳은 0, 칸막이가 존재하는 부분은 1로 표시
#0이 상하좌우로 붙은 경우 연결된 것으로 간주
#이때 얼음 틀 모양이 주어졌을 때 생성되는 총 얼음의 개수

#1. 첫 번째 줄에 얼음 틀의 세로길이 N과 가로길이 M이 주어짐(1이상 1,000이하)
#2. 두 번째 줄부터 N+1번째 줄까지 얼음틀의 형태가 주어짐
#3. 구멍 = 0, 아닌 곳 = 1

#출력 조건 : 한 번에 만들 수 있는 얼음 개수를 출력

print('얼음틀의 사이즈를 입력')
N, M = map(int, input().split())

case = [[0] * M for _ in range(N)]

for i in range(N):
    case[i] = list(map(int, input().split()))

print(case)

#0인 값들을 노드 처리를 해야할텐데 어떻게?


