T = int(input())
for t in range(T):
    N, S = map(int, input().split())
    game = [[0]*N for _ in range(N)]
    out = [[0]*N for _ in range(N)]
    for n in range(N):
        game[n] += list(map(int, input().split()))

    if S == 'up':

# 너무 힘들다아아아아아아아아아아아아아아아아아아아아아아아아