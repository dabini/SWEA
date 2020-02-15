for t in range(10):
    num = int(input())  #회문길이
    field = [[0]*8 for _ in range(8)]

    for k in range(8):
        field[k] = list(map(str, input()))

    res = True
    cnt = 0
    for y in range(8):
        lst = []
        lst2 =[]
        for x in range(8):
            lst += [field[y][x]]
            lst2 += [field[x][y]]

        for n in range(0, (8 - num) +1):
            out = []
            out2 = []
            for m in range(n, n+num):
                out += lst[m]
                out2 += lst2[m]

            if out == out[::-1]:
                cnt += 1

            if out2 == out2[::-1]:
                cnt += 1
    print("#{} {}".format(t+1, cnt))