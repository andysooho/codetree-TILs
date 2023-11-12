k = int(input())
board = [[0]*5 for _ in range(5)]
visited = [[False]*5 for _ in range(5)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0

for _ in range(k):
    r,c = map(int,input().split())
    board[r-1][c-1] = -1

visited[0][0] = visited[4][4] = True

if k & 1:
    print(0)
    exit()

def check():
    global board, visited
    for i in range(5):
        for j in range(5):
            if board[i][j] != -1 and not visited[i][j]:
                return 0
    return 1

def backtracking(a,b):
    global board, visited
    if a == b:
        return check()

    count = 0
    for i in range(4):
        na = (a[0] + dx[i], a[1] + dy[i])
        if not (0 <= na[0] < 5) or not (0 <= na[1] < 5) or board[na[0]][na[1]] == -1 or visited[na[0]][na[1]]:
            continue
        for j in range(4):
            nb = (b[0] + dx[j], b[1] + dy[j])
            if not (0 <= nb[0] < 5) or not (0 <= nb[1] < 5) or board[nb[0]][nb[1]] == -1 or visited[nb[0]][nb[1]]:
                continue
            visited[na[0]][na[1]] = visited[nb[0]][nb[1]] = True
            count += backtracking(na, nb)
            visited[na[0]][na[1]] = visited[nb[0]][nb[1]] = False
    return count


print(backtracking((0, 0), (4, 4)))