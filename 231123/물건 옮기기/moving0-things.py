from collections import defaultdict

counter = defaultdict(list)
n = int(input())

for _ in range(n):
    num,side = map(int,input().split())
    if len(counter[num]) == 0:
        counter[num].append(side)
    else:
        if counter[num][-1] != side:
            counter[num].append(side)

answer = 0
for i in counter:
    if len(counter[i]) > 1:
        answer += len(counter[i]) - 1

print(answer)