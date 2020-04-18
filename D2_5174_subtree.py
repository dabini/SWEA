def check(N):
    global cnt
    if arr[N][0]:
        cnt += 1
        check(arr[N][0])
    if arr[N][1]:
        cnt += 1
        check(arr[N][1])

T = int(input())
for t in range(T):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    arr = [[0]*2 for _ in range(E+2)]
    for i in range(E):
        if not arr[lst[2*i]][0]:
            arr[lst[2*i]][0] = lst[2*i+1]
        else:
            arr[lst[2*i]][1] = lst[2*i+1]
    print(arr)
    cnt = 1
    check(N)
    print("#{} {}".format(t+1, cnt))