T = int(input())
for t in range(T):
    K, N, M = map(int, input().split())
    busstops = list(map(int, input().split()))
    lst = [0] *  (N+1)

    for i in range(len(busstops)):
        lst[busstops[i]] += 1

    start = 0
    end = K
    cnt = 0

    while True:
        zero = 0
        for i in range(start +1, end+1) :
            if lst[i] == 1:
                start = i
            else:
                zero += 1
        if zero == K:
            cnt = 0
            break
        cnt += 1
        end = start + K

        if end >= N:
            break
    print('#{0} {1}'.format(t+1, cnt))