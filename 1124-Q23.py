#국영수
#학생 N명의 이름과 국어, 영어, 수학 점수가 주어짐
#다음 조건으로 성적을 정렬
#1. 국어 점수가 감소하는 순서로
#2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
#3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
#4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로

#입력 조건
#1. 첫 줄에 반 학생 수 N 입력
#2. 다음 줄부터 학생 이름, 국어, 영어, 수학 점수가 공백으로 구분해 주어짐
#3. 점수는 1이상 100이하 자연수
#4. 이름은 문자열로 길이는 10자리를 넘지 않음

#출력 조건 : N개의 줄에 걸쳐 각 학생의 이름을 출력

print('학생 수 입력')
N = int(input())

print('성적 정보 입력\n이름 국어 영어 수학')
score = []
for i in range(N):
    score.append(list(map(str, input().split())))
    for j in range(1, 4):
        score[i][j] = int(score[i][j])

print(score)

for i in range(1, N):
    for j in range(i):
        #국어 점수 오름차순
        if score[i][1] > score[j][1]:
            score[i], score[j] = score[j], score[i]
        elif score[i][1] == score[j][1]:
            #영어 점수 내림차순
            if score[i][2] < score[j][2]:
                score[i], score[j] = score[j], score[i]
            elif score[i][2] == score[j][2]:
                #수학 점수 오름차순
                if score[i][3] > score[j][3]:
                    score[i], score[j] = score[j], score[i]
                elif score[i][3] == score[j][3]:
                    if score[i][0] < score[j][0]:
                        score[i], score[j] = score[j], score[i]

for i in range(N):
    print(score[i][0])

#자체 평가 : 어렵지 않았음