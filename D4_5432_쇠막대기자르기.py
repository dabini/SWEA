T = int(input())
for t in range(T):
    check = list(input())
    cnt = 0
    stack = []
    for c in range(len(check)):
        if check[c] == "(":
            stack.append(1)
        else:
            stack.pop()
            if check[c-1] == '(':
                cnt += len(stack)
            else:
                cnt += 1
    print("#{} {}".format(t+1, cnt))