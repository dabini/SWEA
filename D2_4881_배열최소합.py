T = int(input())

def FindSome(y):
    global N, ans, res
    if y >= N:
        if ans < res:
            res = ans
        return
    for x in range(N):
        if not visited[x] and ans+mymap[y][x] < res:
            visited[x] = 1
            ans += mymap[y][x]
            FindSome(y+1)
            visited[x] =0
            ans -= mymap[y][x]


for t in range(T):
    N = int(input())
    mymap = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    res = 987654321
    ans = 0
    FindSome(0)
    print("#{} {}".format(t+1, res))