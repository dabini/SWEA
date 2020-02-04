A = list(range(1, 13))

T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    cnt = 0
    for i in range(1<<len(A)):
        out = []
        total = 0
        for j in range(len(A)):
            if i & (1<<j):
                out.append(A[j])
        for a in range(len(out)):
            total += out[a]
        if total == K and len(out) == N:
            cnt += 1
    print("#{} {}".format(t+1, cnt))