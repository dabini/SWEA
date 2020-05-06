def find(curx, cury, cnt):
    global min_cnt

    if curx == N-1 and cury == N-1:
        if min_cnt > cnt:
            min_cnt = cnt
            return

    if curx +1 < N:
        find(curx+1, cury, cnt+arr[cury][curx+1])

    if cury +1 < N:
        find(curx, cury+1, cnt+arr[cury+1][curx])


T = int(input())
for t in range(T):
    N = int(input())
    arr = []
    for n in range(N):
        arr.append(list(map(int, input().split())))
    # print(arr)
    min_cnt = 987654321
    find(0, 0, arr[0][0])
    print("#{} {}".format(t+1, min_cnt))