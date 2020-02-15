def magnetic(lst):
    if lst[-1] == 1:
        lst.pop()
        return magnetic(lst)
    elif lst[0] == 2:
        lst.pop(0)
        return magnetic(lst)

for t in range(10):
    N = int(input())

    table = [[0]*N for _ in range(N)]

    for i in range(N):
        table[i] = list(map(int, input().split()))  #1 = N극 2 = S극

    cnt = 0
    for y in range(N):
        lst = []
        for x in range(N):
            if table[x][y] > 0:
                lst.append(table[x][y])
        magnetic(lst)

        start = 1
        for i in range(1, len(lst)):
            if lst[i-1] ==1 and lst[i] ==2:
                cnt += 1
    print("#{} {}".format(t+1, cnt))