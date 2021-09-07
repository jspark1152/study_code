#실전 문제 : 부품 찾기
#동빈이네 전자 매장에는 부품이 N개
#각 부품은 정수 형태의 고유한 번호가 있음
#손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청
#이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성

#첫 줄에 정수 N 입력(1이상 1,000,000이하)
#두번째 줄에 공백으로 구분하여 N개의 정수를 입력, 정수는 1보다 크고 1,000,000 이하
#셋째 줄에는 정수 M 입력(1이상 100,000이하)
#넷째 줄에는 공백으로 구분하여 M개의 정수를 입력, 정수는 1보다 크고 1,000,000 이하

#출력 조건 : 첫 줄에 공백으로 구분하여 각 부품이 존재하면 yes, 없으면 no 출력

print('매장에서 보유중인 부품 종류 수 N 입력')
N = int(input())

print('매장에서 보유중인 부품 번호 입력')
lib_store = list(map(int, input().split()))

print('손님이 구매하고자 하는 부품 종류 수 M 입력')
M = int(input())

print('손님이 구매하고자 하는 부품 번호 입력')
lib_client = list(map(int, input().split()))

result = []

for i in range(M):
    for j in range(N):
        if lib_client[i] == lib_store[j]:
            result.append('yes')
    if len(result) != i+1:
        result.append('no')

for k in range(len(result)):
    print(result[k], end=' ')    

#자체 평가 : 쉬웠음. 일단 순차 탐색으로 풀이.
#이진 탐색으로 가능? 해보자
#바로 안떠오르네

lib_store = sorted(lib_store)
lib_client = sorted(lib_client)
print(lib_store)
print(lib_client)


def bin_sol(start, end):
    result = []
    for i in range(M):
        target = lib_client[i]

        while start <= end:
            mid = (start+end)//2
            if target == lib_store[mid]:
                result.append('yes')
            elif target < lib_store[mid]:
                end = mid-1
            elif target > lib_store[mid]:
                start = mid+1
        
        if len(result) != i+1:
            result.append('no')

bin_sol(0, N-1)

for i in range(len(result)):
    print(result[i], end=' ')

#자체 평가 : 제대로 한게 맞나 암튼 음 자료가 많이 주어질때는 이진 탐색이 빠르다는거?
