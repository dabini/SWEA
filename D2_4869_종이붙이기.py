T = int(input())

for t in range(T):
    N = int(input())
    cnt = 0

    if N % 20:
        cnt += 4**(N//20)
    else:
        cnt += 2**(N//20)

    cnt += 1

    print("#{} {}".format(t+1, cnt))