from collections import Counter
import sys

n = int(input())
arr = []

for _ in range(n):
    temp = sorted(list(map(str,sys.stdin.readline().rstrip().split())))
    arr.append(''.join(temp))

counter = Counter(arr)
print(counter.most_common(1)[0][1])