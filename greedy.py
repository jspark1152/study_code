#그리디(Greedy)
#현재 상황에서 지금 당장 좋은 것만 고르는 방법
#이 유형은 암기와 별개로 창의력이 필요

#거스름돈
#카운터에는 거스름돈으로 사용될 500, 100, 50, 10 동전히 무한히 존재
#손님에게 거슬러 줘야 할 돈이 N원일 때 동전의 최소 개수를 구하라
#단, N은 항상 10의 배수.

print('거스름 돈 액수 입력')
N = int(input())

a, b, c, d = [0, 0, 0, 0]

#동전 수를 최소화하기 위해 가장 금액이 큰 동전부터 처리
while N >= 500:
    N -= 500
    a += 1

while N >= 100:
    N -= 100
    b += 1

while N >= 50:
    N -= 50
    c += 1

while N >= 10:
    N -= 10
    d += 1

print('거스름 돈 동전 개수는 총 {} 개.'.format(a+b+c+d))
#자체 피드백 : 생각보다 깔끔하게 잘 짠듯

#모범 답안
n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)
#너무 깔끔하네 복잡도도 이 방법이 낮아보임

#그리디 실전 문제 1 : 큰 수의 법칙
#다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
#단, 배열의 특정 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없음
#예를 들어 [2,3,4,5,6] / M=8 / K=3 >> 6+6+6+5+6+6+6+5 = 46
#단, 인덱스는 다르지만 값이 같은 경우 서로 다른 것으로 간주함

#배열의 크기 N, 더해지는 횟수 M, 그리고 조건 K

#첫째 줄에 N(2이상 1000이하), M(1이상 10,000이하), K(1이상 10,000)의 자연수가 주어지며 공백으로 구분
#둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분. 각 자연수는 1이상 10,000 이하
#K <= M

#출력조건 : 큰 수의 법칙에 따라 더해진 답을 출력

print('N, M, K를 순서대로 입력')
N, M, K = map(int, input().split())

print('{} 개의 자연수를 입력'.format(N))
numb = []*N
numb = list(map(int, input().split()))

print(numb)

numb.sort() #정렬이 포인트.

print(numb)

result = 0
m = 0
n = 0
if K == M:
    result = K*numb[N-1]
else:
    m = M // (K+1)
    n = M % (K+1)
    result = m*(K*numb[N-1]+numb[N-2]) + n*numb[N-1]

print(result)
#자체 평가 : 10분도 안걸림
#N개의 자연수를 입력하는 과정에서 잠시 문제 발생. numb 리스트 명칭을 list로 했었는데 이때문에 문제 발생;;;
#명칭 정의에도 조심해야할듯
#모범 답안과도 큰 차이는 없음

#그리디 실전 문제 2 : 숫자 카드 게임
#여러 숫자 카드 중 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
#아래의 룰을 따름
#1. 숫자가 쓰인 카드를 N X M 형태로 둠
#2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택
#3. 선택된 행에 포함된 카드들 중 가장 낮은 숫자 카드를 뽑아야함
#4. 따라서 처음 행을 선택할 때, 이후 행에서 낮은 숫자 카드를 뽑을 것을 고려해야함

#첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 각각 자연수로 입력(1이상 100이하)
#둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1 이상 10,000 이하 자연수

#출력 조건 : 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.

print('카드 배열 N X M 지정')
N, M = map(int, input().split())

print('성분 입력')
mat_nm = [[0]*M for _ in range(N)]

for i in range(N):
    mat_nm[i] = list(map(int, input().split()))
    mat_nm[i].sort()

print(mat_nm)

mat_n1 = [mat_nm[i][1] for i in range(N)]
mat_n1.sort()

print(mat_n1[0])
#자체 평가 : 10분도 안걸림
#일단 주어진 행별로 원소를 정렬
#각 행의 1열 성분들이 각 행에서의 최소값 > 따라서 1열의 원소들만 비교
#모범 답안에선 입력된 행에서 바로 최소값을 처리

result = 0
for i in range(N):
    data = list(map(int, input().split()))
    min_val = min(data)

    result = min(result, min_val)
print(result)
#더 간단해보임

#그리디 실전 문제 3 : 1이 될 때까지
#어떠한 수 N이 1이 될 때 까지 다음 두 과정 중 하나를 반복 수행
#1. N - 1
#2. N / K if N % K == 0

#첫째 줄에 N(2이상 100,000이하)과 K(2이상 100,000이하)가 공백으로 구분, 단 N>=K

#출력 조건 : 첫째 줄에 N이 1이 될 때 까지 과정 중 최소 횟수 출력

print('N과 K 값을 입력')
N, K = map(int, input().split())

#수를 줄여가는데 있어서 나누기가 가장 적합 > 즉, 항상 먼저 수행
count=0
while N != 1:
    if N % K == 0:
        N = N / K
        count += 1
    else:
        N -= 1
        count += 1

print(count)
#자체 평가 : 10분도 안걸림
#너무 간단했음
#모범 답안보다 나아보임

#문득 든 생각
#이 문제는 그냥
N, K = map(int, input().split())

count = N//K + N%K 

#아닌가? 어이가 없음ㅋㅋㅋ