#모험가 길드
#N명의 모험가를 대상으로 공포도를 측정
#공포도가 높은 모험가는 수비게 공포를 느껴 위험 상황 대처 능력이 떨어짐
#공포도가 X인 모험가는 반드시 X명 이상으로 구성
#최대 몇 개의 모험가 그룹을 만들 수 있을지
#입력 조건
#1. 첫 줄에 모험가 수 N 입력
#2. 둘째 줄에 공포도 값을 N 이하의 자연수로 공백 구분하여 입력
#출력 조건 : 여행 떠날 수 있는 그룹 수 최댓값을 출력

print('모험가 수 N 입력')
N = int(input())

print('공포도 정보 입력')
fear = list(map(int, input().split()))

#음.. 어떤 방향으로 풀이를 하면 좋을까
#공포도가 작은 사람부터 처리?

fear.sort()

print(fear)

result = 0 
count = 0

for i in fear:
    count += 1
    if count == i:
        result += 1
        count = 0

print(result)


#아이디어 기억해두자