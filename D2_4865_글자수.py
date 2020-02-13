T = int(input())

for t in range(T):
    str1 = input()
    str2 = input()

    dict = {}
    for s in str1:
        dict[s] = str2.count(s)

    maxv = 0
    for k, v in dict.items():
        if v > maxv:
            maxv = v

    print("#{} {}".format(t+1, maxv))