T = int(input())

for t in range(T):
    N = int(input())

    busstop = [0] * 5001

    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1):
            busstop[j] += 1
    res = []
    P = int(input())
    for p in range(1, P+1):
        c = int(input())
        res.append(busstop[c])
    print("#{}".format(t+1), end = ' ')
    print(*res)