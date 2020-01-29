TC = int(input())
for tc in range(TC):
    N = int(input())
    a = list(map(int, input()))
    cnt_lst = [0]*10

    for i in range(N):
        cnt_lst[a[i]] += 1

    max_idx, max_num = 0, 0
    for i in range(len(cnt_lst)-1,-1,-1):
        if cnt_lst[i] > max_idx:
            max_idx = cnt_lst[i]
            max_num = i

    print('#{0} {1} {2}'.format(tc+1, max_num, max_idx))