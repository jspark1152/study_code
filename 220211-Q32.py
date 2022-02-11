'''
정수 피라미드 삼각형
맨 위층 수부터 시작하여 아래층으로 내려오면서 정수를 하나씩 선택
선택된 각 층의 수들의 합이 최대가 되게

입력 조건
1. 첫 줄에 삼각형의 크기 n(1 이상 500 이하), 그 다음줄 부터 정수 삼각형의 정보 입력

출력 조건 : 합이 최대가 되는 경로에 있는 수의 합을 출력
'''

print('삼각형 크기 n 입력')
n = int(input())

tri = []
print('삼각형 정보 입력')
for _ in range(n):
    tri.append(list(map(int, input().split())))

print(tri)
for i in range(1, n):
    for j in range(i+1):
        #좌측에서 내려온 경우
        if j == 0:
            left = 0
        else:
            left = tri[i-1][j-1]
        
        #우측에서 내려온 경우
        if j == i:
            right = 0
        else:
            right = tri[i-1][j]
        
        tri[i][j] = tri[i][j] + max(left, right)

print(tri)

result = 0
for i in range(n):
    result = max(result, tri[n-1][i])

print(result)

#자체 평가 : 층을 거듭할 때마다 최대값 갱신으로 구현, 원하는대로 잘 구현