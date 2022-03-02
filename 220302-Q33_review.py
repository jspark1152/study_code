N = int(input())

info = []
for _ in range(N):
    a, b = map(int, input().split())
    info.append((a, b))

print(info)

dp = [0] * (N+1)
max_val = 0

for i in range(N-1, -1, -1):
    time = info[i][0] + i
    
    if time <= N:
        dp[i] = max(info[i][1]+dp[time], max_val)
        max_val = dp[i]
    else:
        dp[i] = max_val

print(dp)