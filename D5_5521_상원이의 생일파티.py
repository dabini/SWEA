def bfs(v):
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        for n in f_list[v]:
            if not visited[n]:
                q.append(n)
                visited[n] = visited[v] + 1


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    f_list = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    for m in range(M):
        a, b = map(int, input().split())
        f_list[a].append(b)
        f_list[b].append(a)
    bfs(1)
    res = visited.count(2) + visited.count(3)
    print("#{} {}".format(t+1,res))