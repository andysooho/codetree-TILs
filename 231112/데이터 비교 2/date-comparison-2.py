import sys
from collections import Counter

n = int(input())
arr = [sys.stdin.readline().rstrip() for _ in range(2*n-1)]

count = Counter(arr)

for i in count:
    if count[i] == 1:
        print(i)
        break