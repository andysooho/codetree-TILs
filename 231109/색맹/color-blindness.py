import sys
from collections import deque
from pprint import pprint

dx = [1,0,-1,0]
dy = [0,-1,0,1]

n = int(input())
board = [list(map(str,sys.stdin.readline())) for _ in range(n)]
visit_1 = [[0]*n for _ in range(n)]
visit_2 = [[0]*n for _ in range(n)]
answer_1 = 0
answer_2 = 0

def bfs(s,e,visited):
    global n,board
    q = deque()
    q.append((s,e))
    visited[s][e] = 1
    color = board[s][e]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not 0<=nx<n or not 0<=ny<n:
                continue
            if board[nx][ny] == color and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = 1


for i in range(n):
    for j in range(n):
        if visit_1[i][j] == 0:
            bfs(i,j,visit_1)
            answer_1 +=1

for i in range(n):
    for j in range(n):
        if board[i][j] == 'G':
            board[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if visit_2[i][j] == 0:
            bfs(i,j,visit_2)
            answer_2 +=1

print('{} {}'.format(answer_1,answer_2))