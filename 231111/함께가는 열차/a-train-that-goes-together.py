import sys

n = int(input())
arr = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

stack = []

for i in range(n-1,-1,-1):
    if not stack:
        stack.append(arr[i][1])

    elif stack[-1] < arr[i][1]:
        continue
        
    else:
        stack.append(arr[i][1])

print(len(stack))