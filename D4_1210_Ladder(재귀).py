def DFS(a, b):
    global field, t
    field[b][a] = 99
    if b == 0:
        print("#{} {}".format(t, a))
        return
    else:
        if a-1 >= 0 and field[b][a-1] == 1:
            DFS(a-1, b)
        elif a+1 < 100 and field[b][a+1] == 1:
            DFS(a+1, b)
        elif 0 <= b-1 and field[b-1][a] == 1:
            DFS(a, b-1)

for _ in range(10):
    t = int(input())
    field = [[0]*100 for __ in range(100)]

    for i in range(100):
        field[i] = list(map(int, input().split()))

    for x in range(100):
        if field[99][x] == 2:
            start = x


    a = start
    b = 99
    print(DFS(a, b))