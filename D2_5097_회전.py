T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    num_lst = list(map(int, input().split()))
    for m in range(M):
        q = num_lst.pop(0)
        num_lst.append(q)
    print("#{} {}".format(t+1, num_lst[0]))