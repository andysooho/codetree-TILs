import sys

n = int(input())
edges = [0]*(n+1)
for i in range(1,n+1):
    edges[i] = int(sys.stdin.readline().rstrip())

visited = [0]*(n+1)
answer = 0

for i in range(1,n+1):
    if visited[i] != 0:
        continue

    stack = [i]
    while stack:
        cur = stack[-1]
        
        if visited[cur] == 1:
            while stack:
                visited[stack.pop()] = 2
            break
        
        if visited[cur] == 2:
            stack.pop()
        
        else: # == 0
            visited[cur] = 1
            next = edges[cur]
            
            if visited[next] == 0 and next !=0:
                stack.append(next)
            else:
                visited[cur] = 2
                stack.pop()
    else:
        answer += 1

print(answer)