from collections import defaultdict

n = int(input())
s = list(map(str,input().split()))

count = defaultdict(lambda:0)
count[s[0]] = 1

for i in range(1,n):
    if s[i] != s[i-1]:
        count[s[i]] += 1

print(1+min(count['a'],count['b']))