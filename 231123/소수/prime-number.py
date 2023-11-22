a,b = map(int,input().split())

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

count = 0
min_val = 1e9
for num in range(a,b+1):
    if is_prime(num):
        count += num
        min_val = min(min_val, num)

if not count:
    print(-1)
    exit()
print(count)
print(min_val)