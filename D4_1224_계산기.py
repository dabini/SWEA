isp = {'(' : 0, '+' : 1, '*' : 2}
icp = {'(' : 3, '+' : 1, '*' : 2}
for t in range(1, 11):
    num = int(input())
    calc = input()
    num_lst = []
    stack = []
    for c in calc:
        if c.isnumeric():
            num_lst += [c]
        elif c == '(':
            stack += [c]
        elif c == ')':
            while stack and stack[-1] != '(':
                p = stack.pop()
                num_lst += [p]
            stack.pop()
        else:
            while stack and isp[stack[-1]] >= icp[c]:
                num_lst += [stack.pop()]
            stack += [c]
    while stack:
        p = stack.pop()
        if p != '(':
            num_lst += [p]

    stack2 = [0]
    for n in num_lst:
        if n.isnumeric():
            stack2 += [int(n)]
        else:
            if n == '+':
                tmp = stack2[-2] + stack2[-1]
            elif n == '*':
                tmp = stack2[-2] * stack2[-1]
            stack2.pop()
            stack2.pop()
            stack2 += [tmp]
    print("#{} {}".format(t, stack2[1]))