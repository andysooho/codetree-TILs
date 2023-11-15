import sys

n = int(input())
edges = [0]*(n+1)
#각 노드당 연결된 수가 무조건 1개 이하이므로 [[]*(n+1)] 대신에 일차원 인접리스트로 표현
for i in range(1,n+1):
    edges[i] = int(sys.stdin.readline().rstrip())


def dfs(num):
    global visited
    visited[num] = True

    next_node = edges[num]
    if not visited[next_node] and next_node != 0: #다음노드가 존재하고 방문안했다면 
        return dfs(edges[num]) #탐색
    elif next_node == 0: # 끝 노드에 도달
        return True #루프 없음

    return False
    

answer = 0
for i in range(1, n+1):
    visited = [False] * (n+1)
    if dfs(i):
        answer += 1

print(answer)