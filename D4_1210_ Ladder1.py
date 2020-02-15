for _ in range(10):
    tc = int(input())
    field = [[0]*100 for __ in range(100)]

    for i in range(100):
        field[i] = list(map(int, input().split()))

    for x in range(100):
        if field[99][x] == 2:
            start = x
            break
    a = start
    b = 99

    while True:
        if (a-1) >= 0 and field[b][a-1] == 1:
            while (a-1) >= 0 and field[b][a-1] == 1:
                a -=1
            b -=1
        elif (a+1) <= 99 and field[b][a+1] == 1:
            while (a+1) <= 99 and field[b][a+1] == 1:
                a += 1
            b -= 1
        else:
            b -= 1
        if b == 0:
            break
    print("#{} {}".format(tc, a))