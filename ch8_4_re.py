#점화식 아이디어로 다시 풀이

# A_n = A_n-1 + 2A_n-2

N = int(input())

mark = [0] * 1001

mark[1] = 1

mark[2] = 3

for i in range(3, N+1):
    mark[i] = mark[i-1] + 2*mark[i-2]

print(mark[N] % 796796)

#평가 : 점화식 사고를 습관화. 예전 학창시절의 내 머리로 계산하는 점화식이 아님.