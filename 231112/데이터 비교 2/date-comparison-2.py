import sys
from collections import Counter

n = int(input())
arr = [sys.stdin.readline().rstrip() for _ in range(n)]
arr2 = [sys.stdin.readline().rstrip() for _ in range(n-1)]

count = Counter(arr)
count2 = Counter(arr2)

for i in count-count2:
    if count[i] != 0:
        print(i)
        break