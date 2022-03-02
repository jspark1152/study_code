'''
N명의 병사가 무작위로 나열
각 병사는 특정 값의 전투력 보유
병사 배치 시 전투력이 높은 병사가 앞에 오도록 내림차순으로 배치
이는 나열된 병사들 중 특정 병사들을 열외시키는 방법을 통해 진행
단, 남아있는 병사의 수가 최대가 되도록

입력 조건
1. 첫줄에 N이 주어짐
2. 다음 줄에 각 병사의 전투력을 공백으로 구분하여 입력

출력 조건 : 남아 있는 병사들의 수가 최대가 되도록 하는 열외 인원 출력
'''

print('병사 수 N 입력')
N = int(input())

print('병사 전투력 정보 입력')
att = list(map(int, input().split()))
print(att)

max_val = 0

#음 이렇게 하니까 오류 발생
#왜 거꾸로 하면 될거같지..?
#맞나..? 뭐가 다르지?
for i in range(N-1, -1, -1):
    list0 = []
    list0.append(att[i])
    for j in range(i-1, -1, -1):
        if list0[-1] < att[j]:
            list0.append(att[j])
        print(list0)
    max_val = max(len(list0), max_val)

print(N-max_val)

#자체 평가 : 아닌거 같은데 답은 나온다.. 뭔가 분명히 오류가 있을 것인데..