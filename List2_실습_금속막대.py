import itertools

T = int(input())
for t in range(T):
    n = int(input())
    lst = list(map(int, input().split()))

    # print(list(map(list, itertools.permutations(lst))))
    for k in list(map(list, itertools.permutations(lst))):
        for i in range(1, 2*n-2, 2):
            if k[i] == k[i+1]:
                break

    # print("#{} {}".format(t+1, " ".join(out)))