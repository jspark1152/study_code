'''
38. 정확한 순위

N명의 성적 분실, 성적을 비교한 결과 일부만 존재
N명의 성적은 모두 다름

A번 학생의 성적이 B번 학생보다 낮으면 A에서 B로 가리키도록 표현
성적을 비교한 결과가 주어질 때, 성적 순위를 정확히 알 수 있는 학생은 몇 명인지 출력

입력 조건
1. 첫 줄에 학생들의 수 N(2이상 500이하)과 두 학생 성적 비교 횟수 M(2이상 10,000이하) 입력
2. 다음 M개의 줄에 성적 비교를 입력. A B = A성적 < B성적

출력 조건 : 성적 순위를 정확히 알 수 있는 학생이 몇명인지 출력
'''

#A >> B 비교. A에서 B로 이동 가능. 최단 거리 문제로 볼 수 있음.
#단 가능 여부를 0 으로 봄
#score[a][b] = 0 : a 번 학생 성적 < b 번 학생 성적

print('학생 수 N과 성적 비교 자료 수 M 입력')
N, M = map(int, input().split())

INF = int(1e9)
score = [[INF]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    score[i][i] = 0

print('성적 비교 자료 A B 입력')
for _ in range(M):
    A, B = map(int, input().split())
    score[A][B] = 0

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            score[a][b] = min(score[a][b], score[a][k]+score[k][b])

print(score)

result = 0

for i in range(1, N+1):
    point = 0
    for j in range(1, N+1):
        if score[i][j] == 0 or score[j][i] == 0:
            point += 1
    if point == 6:
        result += 1 #최종적으로 본인 포함 모든 학생들과 비교가 가능(이동이 가능)한 경우를 의미

print(result)