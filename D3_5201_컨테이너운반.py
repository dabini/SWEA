T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    w_lst = list(map(int, input().split()))
    t_lst = list(map(int, input().split()))
    w_lst.sort(reverse=True)
    t_lst.sort(reverse=True)

    res = 0
    for t in t_lst:
        for w in w_lst:
            if w <= t:
                res += w
                w_lst.remove(w)
                break
    print("#{} {}".format(tc+1, res))