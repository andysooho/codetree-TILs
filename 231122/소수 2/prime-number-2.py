n = int(input())

visited = [True] * (n+1)
prime = []

for i in range(2,n+1):
    if visited[i]:
        prime.append(i)
        temp = 1
        while temp * i < n+1:
            visited[temp * i] = False
            temp += 1

print(len(prime))