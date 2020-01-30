T = int(input())

for t in range(T):
    N = int(input())
    pri_lst = list(map(int, input().split()))
    start = pri_lst[-1]
    res = 0
    for n in range(N-1, -1, -1):
        if start >= pri_lst[n]:
            res += start - pri_lst[n]
        else:
            start = pri_lst[n]
            res += start - pri_lst[n]

    print("#{} {}".format(t+1, res))