T = int(input())

for t in range(T):
    tests = list(map(str, input()))
    stack = [0]
    res = [0] * 128
    res[ord('}')] = '{'
    res[ord(')')] = '('
    for i in range(len(tests)):
        if tests[i] == '{' or tests[i] == '(':
            stack += [tests[i]]
        elif (tests[i] == '}' or tests[i] == ')'):
            stack += [tests[i]]
            if res[ord(tests[i])] == stack[-2]:
                stack.pop()
                stack.pop()

    if stack[-1] == 0:
        ans = 1
    else:
        ans = 0

    print("#{} {}".format(t+1, ans))