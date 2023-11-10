n = int(input())
arr = [input() for _ in range(n)]

arr.sort(key= lambda x:len(x))
print('\n'.join(arr))