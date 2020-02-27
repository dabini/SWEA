T = int(input())
for t in range(T):
    N = int(input())
    tmp = []
    field = [list(map(int, input().split())) for _ in range(N)]
    res = []

    for y in range(N):
        for x in range(N):
            if field[y][x] != 0:
                j = y
                i = x
                while i <N and field[y][i] != 0 :
                    i += 1
                while  j < N and field[j][x] != 0:
                    j += 1
                tmp.append([j-y, i-x, (j-y)*(i-x)])
                for a in range(y, j):
                    for b in range(x, i):
                        field[a][b]= 0
    # print(tmp)
    for k in range(len(tmp)):
        min_num = tmp[k][2]
        for c in range(k+1, len(tmp)):
            if tmp[c][2] < min_num:
                min_num = tmp[c][2]
                tmp[k], tmp[c] = tmp[c], tmp[k]
            elif tmp[c][2] == min_num:
                if tmp[k][0] > tmp[c][0]:
                    tmp[k], tmp[c] = tmp[c], tmp[k]

    # print(tmp)
    for r in tmp:
        res.append(str(r[0]))
        res.append(str((r[1])))
    print("#{} {} {}".format(t+1, len(tmp), ' '.join(res)))