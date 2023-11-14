string = input()
t = input()

stack = []

for c in string:
    stack.append(c)
    if len(stack) >= len(t):
        if ''.join(stack[-len(t):]) == t:
            for _ in range(len(t)):
                stack.pop()

print(''.join(stack))