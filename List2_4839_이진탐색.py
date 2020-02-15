T = int(input())
for t in range(T):
    P, A, B = map(int, input().split())

    def book(P, X):
        l = 1
        r = P
        c = int((l + r) / 2)
        cnt = 1
        while l <= r:
            if c == X:
                break
            elif c > X:
                cnt += 1
                r = c
                c = int((l + r) / 2)
            elif c < X:
                cnt += 1
                l = c
                c = int((l + r) / 2)
        return cnt

    if book(P, A) < book(P, B):
        res = "A"
    elif book(P, A) > book(P, B):
        res = "B"
    elif book(P, A) == book(P, B):
        res = 0

    print("#{} {}".format(t+1, res))