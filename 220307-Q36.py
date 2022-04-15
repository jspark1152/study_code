'''
주어준 두 문자열 A, B에 대하여
A를 편집하여 B로 만들고자 함
편집 시 사용되는 연산은 3가지
1. 삽입 : 특정 위치에 하나의 문자 삽입
2. 삭제 : 특정 위치에 하나의 문자 삭제
3. 교체 : 특정 위치에 하나의 문자를 다른 문자로 교체
이 때 문자열 A를 B로 만드는 최소 편집 거리를 계산

입력 조건
1. 두 문자열 A, B가 한 줄에 하나씩 주어짐
2. 각 문자열은 영문으로만 구성되어 있으며 문자열의 길이는 1 이상 5000 이하

출력 조건 : 최소 편집 거리를 출력
'''

print('A = ')
A = str(input())

print('B = ')
B = str(input())

print(A, B)

def edit_dist(A, B):
    N = len(A)
    M = len(B)
    
    dp = [[0]*(M+1) for _ in range(N+1)]
    
    for i in range(1, N+1):
        dp[i][0] = i
    for j in range(1, M+1):
        dp[0][j] = j
    
    for i in range(1, N+1):
        for j in range(1, M+1):
            #문자가 같은 경우
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1]
            #다른 경우
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[N][M]

print(edit_dist(A, B))

#자체 평가 : 흠.. 이 방식을 그냥 외우는게 속편할듯.. 아무리 고민해봐도 알고리즘이 안떠오를땐 이 방식을 기계적으로 떠올려야 할듯