# import sys
# sys.stdin = open('input.txt', 'r')

def increase(k):
    k = str(k)
    for a in range(len(k)-1):
        if (int(k[a])) <= int(k[a+1]):
            pass
        else:
            return False
    return True

T = int(input())
for t in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    out = [-1]

    for i in range(N-1):
        for j in range(i+1, N):
            if increase(num_list[i] * num_list[j]):
                out += [num_list[i] * num_list[j]]

    # for a in lst:
    #     for b in range(len(a)-1):
    #         if (int(a[b])) <= int(a[b+1]):
    #             out += [int(a)]

    print("#{} {}".format(t+1, max(out)))