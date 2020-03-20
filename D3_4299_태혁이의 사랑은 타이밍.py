T = int(input())
for t in range(T):
    d, h, m = map(int, input().split())
    res = 0
    check = 11*24*60 + 11*60 + 11
    time = d*24*60 + h*60 + m
    if time - check <0:
        res = -1
    else:
        res = time-check

    print("#{} {}".format(t+1, res))