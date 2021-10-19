#문자열 뒤집기
#0과 1로만 이루어진 문자열 S
#문자열 S에 있는 모든 숫자를 전부 같게 만들 계획
#1은 0 / 0은 1로 변환 가능
#연속된 i번째에서 j번째까지를 뒤집기가 가능

#입력 조건
#1. 첫줄에 0과 1로 이루어진 문자열 S가 주어짐.

#출력 조건 : 첫 줄에 모든 숫자를 같은 수로 만드는데 수행되는 행동 최소 회수 출력

#음.. 이거 바로 안떠오른다..

print('문자열 입력')
N = list(map(int, input()))

A = N
B = N

result0 = 0
result1 = 0

count = 0

for i in range(len(A)):
    if A[i] == 0:
        count = 0
        pass
    else:
        if count == 0:
            result0 += 1
        count += 1

print(result0)

count =0
for i in range(len(B)):
    if B[i] == 1:
        count = 0
        pass
    else:
        if count == 0:
            result1 += 1
        count += 1

print(result1)

print(min(result0, result1))

#자체 평가 : 음 일단 완료. 0으로 통일 / 1로 통일 이 2가지 경우의 최소값을 출력하는 방향으로