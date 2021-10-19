#만들 수 없는 금액
#N개의 동전을 가지고 있음
#이 때 동전들을 이용하여 만들 수 없는 금액 중 최솟값

#입력 조건
#1. 첫 줄에 동전의 개수 N을 입력
#2. 둘째 줄에 화 폐 단위 정보를 공백으로 구분하여 입력

#출력 조건 : 첫 줄에 주어진 동전들로 만들 수 없는 양의 정수 금액 중 최솟값 출력

print('동전 개수 N 입력')
N = int(input())

print('화폐 단위 입력')
cash = list(map(int, input().split()))

cash.sort()

target = 1

for x in cash:

    if target < x:
        break
    target += x

print(target)

#어렵네 이거 ;;