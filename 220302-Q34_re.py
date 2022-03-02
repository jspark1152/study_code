N = int(input())

att = list(map(int, input().split()))

att.reverse()

print(att)

dp = [1] * N
max_val = 1

for i in range(1, N):
    if att[i] > att[i-1]:
        dp[i] = max_val + 1
        max_val = dp[i]
    else:
        pass

print(dp)

print(N - max(dp))

#단조 부분 수열 중 가장 긴 수열을 찾는 알고리즘