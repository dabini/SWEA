for t in range(10):
    V, E = map(int, input().split())
    V_lst = list(map(int, input().split()))

    # lst = []
    # for i in range(0, len(V_lst)-1, 2):
    #     lst += [(V_lst[i], V_lst[i+1])]
    # print(lst)

    max_num = max(V_lst)
    # print(max_num)
    field = [[0] * (max_num+1) for _ in range(max_num+1)]

    # print(field)
    indeg = [0]* (max_num+1)
    outdeg = [0]* (max_num+1)
    for i in range(0, len(V_lst)-1, 2):
        start = V_lst[i]
        end = V_lst[i+1]
        field[start][end] += 1
        indeg[end] += 1
        outdeg[start] += 1

    # print(field)
    # print(indeg)
    # print(outdeg)
    res = [0] * 2
    for y in range(max_num+1):
        for x in range(max_num+1):
            if field[y][x] == 1:
                if indeg[y] == 0 and outdeg[x] >=1:
                    res[0] = str(y)
                    res[1] = str(x)
                    outdeg[y] -= 1
                    # indeg[x] = -1
                elif indeg[x] > 0 and outdeg[x]>=0:
                    res += [str(x)]
                    outdeg[x] -= 1
                # elif indeg[y] > 0 and outdeg[x]>=0:
                #     res += [str(x)]
                #     outdeg[x] -= 1
    print("#{} {}".format(t+1, " ".join(res)))
