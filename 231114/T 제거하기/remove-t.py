s = input()
t = input()

t_hash = hash(t)

def simple_rabin_carp(s):
    global t, t_hash
    stack = []
    i=0
    while i < len(s):
        if s[i] != t[0]:
            stack.append(s[i])
            i += 1
        elif hash(s[i:i+len(t)]) == t_hash:
            i += len(t)
        else:
            stack.append(s[i])
            i += 1

    return ''.join(stack)


answer = simple_rabin_carp(s)
while True:
    before_answer = hash(answer)
    answer = simple_rabin_carp(answer)
    if before_answer == hash(answer):
        print(answer)
        break