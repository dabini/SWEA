def find(n, k):
    global res
    if k == num:
        tmp = ''
        for i in range(n):
            tmp += str(data[i])

        if int(tmp) > res:
            res = int(tmp)
    else:
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                data[i], data[j] = data[j], data[i]
                find(n, k + 1)
                data[i], data[j] = data[j], data[i]


T = int(input())
for t in range(T):
    data, num = map(int, input().split())
    data = [i for i in str(data)]
    n = len(data)
    res = -1
    if num > 5 :
        if num % 2:
            num = 5
        else:
            num = 4
    find(n, 0)
    print('#{} {}'.format(t+1, res))
