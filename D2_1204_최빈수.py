T = int(input())

for t in range(T):
    tc = int(input())
    a = list(map(int, input().split()))
    lst = []

    for ele in a:
        if ele not in lst:
            lst.append(ele)

    cnt_lst = [0] * len(lst)

    for i in range(len(lst)):
        cnt = a.count(lst[i])
        cnt_lst[i] = cnt

    idx = cnt_lst.index(max(cnt_lst))
    # print(cnt_lst)
    print('#{0} {1}'.format(tc, lst[idx]))