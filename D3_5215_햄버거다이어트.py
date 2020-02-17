def backtrack(a, k, input):
    global score_lst, res, L, kal_lst, res
    if k == input:
        psum = 0
        for i in range(input):
            if a[i] == 1:
                psum +=  kal_lst[i]
        if psum < L:
            total = 0
            for i in range(input):
                if a[i] == 1:
                    total += score_lst[i]
            if res < total:
                res = total
                return
    else:
        a[k] = 0
        backtrack(a, k+1, input)
        a[k]= 1
        backtrack(a, k+1, input)

T = int(input())

for t in range(T):
    N, L = map(int, input().split())
    a = [0] * N
    score_lst = []
    kal_lst = []

    for n in range(N):
        score, kal = map(int, input().split())
        score_lst += [score]
        kal_lst += [kal]

    res = 0
    backtrack(a, 0, N)
    print("#{} {}".format(t+1, res))