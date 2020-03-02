def DFS(n):
    global tmp, max_tmp, min_tmp,N
    if n >= N:
        if max_tmp < tmp:
            max_tmp = tmp
        if min_tmp > tmp:
            min_tmp = tmp
        return
    for i in range(4):
        if op_list[i] > 0:
            op_list[i] -= 1
            res = tmp

            if i == 0:
                tmp += num_list[n]
            elif i == 1:
                tmp -= num_list[n]
            elif i == 2:
                tmp *= num_list[n]
            elif i == 3:
                if num_list[n]:
                    tmp = int(tmp/num_list[n])
                # else:
                #     op_list[i] += 1
                #     continue
            n += 1
            DFS(n)
            n -= 1
            tmp = res
            op_list[i] += 1

T = int(input())
for t in range(T):
    max_tmp = -987654321
    min_tmp = 987654321
    N = int(input())
    op_list = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    tmp = num_list[0]
    DFS(1)
    ans = max_tmp - min_tmp
    print("#{} {}".format(t+1, ans))