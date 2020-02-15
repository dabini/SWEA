for _ in range(10):
    t = int(input())

    data = list(map(int, input().split()))

    while True:
        if data[-1] == 0:
            break
        for k in range(1, 6):
            if data[0] - k > 0 :
                new = data[0] - k
                data.pop(0)
                data += [new]
            elif data[0] - k <= 0:
                new = 0
                data.pop(0)
                data += [new]
                break
    data = list(map(str, data))
    print("#{} {}".format(t, " ".join(data)))