board = [list(map(int,input().split())) for _ in range(5)]
v = [[False,False,False,False,False] for _ in range(5)]
orders = list(map(int,input().split()))

def check():
    global v
    count = 0
    for i in range(5):
        if v[0][i] and v[1][i] and v[2][i] and v[3][i] and v[4][i]:
            count += 1
    for i in range(5):
        if v[i][0] and v[i][1] and v[i][2] and v[i][3] and v[i][4]:
            count += 1
    if v[0][0] and v[1][1] and v[2][2] and v[3][3] and v[4][4]:
        count += 1
    if v[4][0] and v[3][1] and v[2][2] and v[1][3] and v[0][4]:
        count += 1
    return count

def find(t):
    global board, v
    for i in range(5):
        for j in range(5):
            if board[i][j] == t:
                v[i][j] = True

for i, t in enumerate(orders):
    find(t)
    if i<12:
        continue
    if check() == 3:
        print(i+1)
        break