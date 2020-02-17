T = int(input())

for t in range(T):
    code = list(map(str, input().split()))

    stack = []
    temp = 0
    res = ''
    for c in range(len(code)):
        if code[c].isnumeric():
            stack.append(int(code[c]))

        else:
            if code[c] == '.':
                break
            if c == (len(code) -1):
                if code[c] != '.':
                    res = 'error'
            if len(stack) < 2:
                res = 'error'
                break
            if code[c] == "+":
                temp = stack[-2] + stack[-1]
            elif code[c] == '-':
                temp = stack[-2] - stack[-1]
            elif code[c] == '*':
                temp = stack[-2] * stack[-1]
            elif code[c] == '/':
                temp = stack[-2] / stack[-1]
            stack.pop()
            stack.pop()
            stack.append(int(temp))
    if len(stack) > 1:
        res = 'error'
    if res != 'error':
        res = stack[0]
    print("#{} {}".format(t+1, res))