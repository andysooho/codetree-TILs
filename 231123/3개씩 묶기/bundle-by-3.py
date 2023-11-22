n = int(input())
arr = [0] + sorted(list(map(int,input().split())),reverse=True)

answer = 0
for i in range(n+1):
    if i % 3:
        answer += arr[i]

print(answer)