n,k = map(int,input().split())

visited = [True] * (n+1)
visited[0] = visited[1] = False

count = 0

for i in range(2,n+1):
    if visited[i]:
        for j in range(i,n+1,i):
            if visited[j]:
                visited[j] = False
                count +=1 
                if count == k:
                    print(j)
                    break
        if count == k:
            break