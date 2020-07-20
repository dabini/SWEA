T = int(input())

for t in range(T):
    L, U, X = map(int, input().split())
    if X > U:
        res = -1
    elif X >= L:
        res = 0
    else:
        res = L - X
    print("#{} {}".format(t+1, res))