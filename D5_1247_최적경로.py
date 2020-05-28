def dfs(l, k , tmp):
    global min_num
    if k == N:
        ans = tmp + abs(l[0] - lst[1][0]) + abs(l[1] - lst[1][1])
        if ans < min_num:
            min_num = ans
            return

    for i in range(N+2):
        if not visited[i]:
            ans = tmp + abs(l[0] - lst[i][0]) + abs(l[1] - lst[i][1])
            if ans > min_num:
                continue
            visited[i] = 1
            dfs(lst[i], k+1, ans)
            visited[i] = 0

T = int(input())
for t in range(T):
    N = int(input())
    loc = list(map(int, input().split()))
    visited = [0] * (N +2)
    visited[0] = visited[1] = 1
    lst = []
    min_num = 987654321
    for i in range(0, N*2+4, 2):
        lst.append([loc[i], loc[i+1]])

    dfs(lst[0], 0, 0)
    print("#{} {}".format(t+1, min_num))