#실전 문제 : 효율적인 화폐 구성

#N가지 화폐
#이 화폐들의 최소 개수를 이용하여 합이 M원이 되도록
#각 화폐는 몇 개라도 사용 가능
#사용한 화폐 구성은 같지만 순서만 다른 것은 같은 경우로 구분

#첫 줄에 N, M이 주어짐(1<=N<=100, 1<=M<=10,000)
#이후 N개의 줄에는 각 화폐의 가치가 주어짐(10,000 이하의 자연수)

#출력 조건 : 첫 줄에 M원을 만들기 위한 최소 화폐 개수를 출력(단, 불가능할시 -1 출력)

print('N 과 M 을 입력')
N, M = map(int, input().split())

money = []
print('화폐 가치 입력')
for i in range(N):
    money.append(int(input()))

money.sort(reverse=True)

print(money)

count = 0

for i in range(len(money)):
    b = M // money[i]

    if b > 0:
        M -= money[i]*b
        count += b
    else:
        pass

if M == 0:
    print(count)
else:
    print(-1)

#자체 평가 : 어렵지 않음.
#오류 발견 : 무조건 큰 화폐부터 시도하다 보니 안맞는 경우가 생김
#ex) N=3 M=10,000   100 / 34 / 109 
#예시 경우 100을 출력해야하나 109부터 계산이 들어가기 때문에 -1 출력
