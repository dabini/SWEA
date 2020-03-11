T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    lst = [0] * N

    for m in range(M):
        for n in range(N):
            if A[n] <= B[m]:
                lst[n] += 1
                break

    res = lst.index(max(lst)) +1
    print("#{} {}".format(t+1, res))