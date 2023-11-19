import sys

n = int(input())
arr = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

dp = [0] * (n+1)

for i in range(n):
    t,p = arr[i]
    if i + t <=n:
        dp[i+t] = max(dp[i+t],dp[i]+p)
    dp[i+1] = max(dp[i+1],dp[1])

print(dp[n])