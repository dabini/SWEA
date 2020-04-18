T= int(input())
for t in range(T):
    N, M, L = map(int, input().split())
    lst = [0] * (N+1)

    for m in range(M):
        nod, num = map(int, input().split())
        lst[nod] = num
    # print(lst)

    if len(lst) % 2:
        lst.append(0)

    for i in range(len(lst)-1, 1, -2):
        lst[i//2] = lst[i] + lst[i-1]


    print("#{} {}".format(t+1, lst[L]))