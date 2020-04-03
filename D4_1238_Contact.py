def BFS(s):
    q.append(s)
    visited[s] = 1

    while q:
        now = q.pop(0)
        for new in range(m):
            if arr[now][new] and not visited[new]:
                q.append(new)
                visited[new] = visited[now] + 1


for test in range(10):
    num, s = map(int, input().split())
    num_lst = list(map(int, input().split()))
    m = max(num_lst) + 1
    arr = [[0]*m for _ in range(m)]
    visited = [0 for _ in range(m)]
    q = []

    for i in range(num//2):
        start, end = num_lst[2*i], num_lst[(2*i)+1]
        arr[start][end] = 1
    BFS(s)

    max_num = -1
    for j in range(m):
        if visited[j] == max(visited):
            if j > max_num:
                max_num = j

    print("#{} {}".format(test+1, max_num))