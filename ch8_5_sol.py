N, M = map(int, input().split())

money = []

for i in range(N):
    money.append(int(input()))

mark = [10001] * (M+1)

mark[0] = 0
for i in range(N):
    for j in range(money[i], M+1):
        if j % money[i] == 0:
            mark[j] = min(mark[j], mark[j-money[i]]+1)

if mark[M] == 10001:
    print(-1)
else:
    print(mark[M])