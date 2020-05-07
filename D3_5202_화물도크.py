T = int(input())
for t in range(T):
    N = int(input())
    lst = []
    tmp = 0
    for n in range(N):
        s, e = map(int, input().split())
        lst.append([s, e])
    lst.sort(key=lambda x: x[1])
    end_time = 0
    while lst:
        s, e = lst.pop(0)
        if s >= end_time:
            tmp += 1
            end_time = e
    print("#{} {}".format(t+1, tmp))