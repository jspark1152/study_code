#소수 구하기
#M 이상 N이하의 소수를 모두 출력
import math

print("1 이상 1,000,000 이하인 수 (M, N)을 입력 : ")
M, N = map(int, input().split())

prime = [i for i in range(2,N+1)]
set = []

print(prime)

for i in range(2, int(math.sqrt(N))+1):
    j = 2
    while i*j <= N:
        set.append(i*j)
        j += 1

prime = [i for i in prime if i not in set]

result = [i for i in prime if M <= i]

for i in range(len(result)):
    print(result[i])