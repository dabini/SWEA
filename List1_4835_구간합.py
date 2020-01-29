T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))

    lst = []
    for k in range(len(a)-M+1):
        total = 0
        for m in range(k, k+M):
            total += a[m]
        lst.append(total)

    max_num = max(lst)
    min_num = min(lst)
    print('#{0} {1}'.format(t+1, max_num-min_num))